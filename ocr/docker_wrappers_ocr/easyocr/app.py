from flask import Flask, request, jsonify
import easyocr

app = Flask(__name__)

reader = easyocr.Reader(['en'])


@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        results = reader.readtext(file.read())

        json_results = []
        for result in results:
            (bbox, text, prob) = result
            bbox = [[int(point) for point in pair] for pair in bbox]
            prob = float(prob)
            json_results.append({'bbox': bbox, 'text': text, 'prob': prob})

        return jsonify({'result': json_results})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
