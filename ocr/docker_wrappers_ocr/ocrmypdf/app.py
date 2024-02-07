from flask import Flask, request, jsonify, send_file
from PIL import Image
import subprocess
import tempfile
import os

app = Flask(__name__)


@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as input_pdf:
        if file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
            image = Image.open(file.stream)
            image.save(input_pdf, 'PDF', resolution=300)
        else:
            file.save(input_pdf)
        input_pdf_path = input_pdf.name

    output_pdf_path = tempfile.mktemp(suffix='.pdf')

    try:
        subprocess.run(['ocrmypdf', '--force-ocr', input_pdf_path, output_pdf_path], check=True)

        grep_result = subprocess.run(['pdfgrep', '.', output_pdf_path], capture_output=True, text=True)
        extracted_text = grep_result.stdout

        response = jsonify({'text': extracted_text})
    except subprocess.CalledProcessError as e:
        response = jsonify({'error': 'Processing failed', 'details': str(e)}), 500
    finally:
        if os.path.exists(input_pdf_path):
            os.remove(input_pdf_path)
        if os.path.exists(output_pdf_path):
            os.remove(output_pdf_path)

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
