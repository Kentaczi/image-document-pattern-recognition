from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)


@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # Read the image via file.stream
        img = Image.open(io.BytesIO(file.read()))
        text = pytesseract.image_to_string(img, lang='eng')

        return jsonify({'text': text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
