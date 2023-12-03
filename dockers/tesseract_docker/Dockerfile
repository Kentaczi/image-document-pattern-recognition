FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y tesseract-ocr

COPY . .

EXPOSE 5000

CMD ["python", "./app.py"]
