from flask import Flask, request, jsonify
from subprocess import Popen, PIPE
import os
import tempfile

app = Flask(__name__)

CALAMARI_CHECKPOINT_PATH = '/path/to/models/'
model_checkpoint = os.environ.get('CALAMARI_MODEL_CHECKPOINT', '4.ckpt.json')
model_path = f'/usr/src/app/{model_checkpoint}'


@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
        file.save(temp_file)
        temp_file_path = temp_file.name

    calamari_cmd = [
        'calamari-predict',
        '--checkpoint', model_path,  # Add more checkpoints if needed
        '--data.images', temp_file_path
    ]

    process = Popen(calamari_cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        return jsonify({'error': 'Calamari OCR failed', 'message': stderr.decode()}), 500

    with open(temp_file_path + '.pred.txt', 'r') as result_file:
        ocr_text = result_file.read()

    os.remove(temp_file_path)
    os.remove(temp_file_path + '.pred.txt')

    return jsonify({'text': ocr_text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
