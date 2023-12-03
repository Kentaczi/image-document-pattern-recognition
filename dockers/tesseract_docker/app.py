from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def do_ocr():
    if 'file' not in request.files:
        return jsonify(error='No file part'), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify(error='No selected file'), 400

    image = Image.open(io.BytesIO(file.read()))
    text = pytesseract.image_to_string(image)
    return jsonify(text=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
