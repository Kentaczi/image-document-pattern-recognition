from flask import Flask, request, jsonify
import keras_ocr
import io
from PIL import Image
import numpy as np

app = Flask(__name__)

pipeline = keras_ocr.pipeline.Pipeline()


@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        image = Image.open(io.BytesIO(file.read()))
        image = np.array(image)

        # Perform OCR
        prediction_groups = pipeline.recognize([image])

        results = [{'text': text, 'box': box.tolist()} for text, box in prediction_groups[0]]

        return jsonify({'results': results})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
