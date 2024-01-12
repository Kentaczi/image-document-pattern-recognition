FROM python:3.8-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ARG BASE_URL="https://raw.githubusercontent.com/Calamari-OCR/calamari_models/master/uw3-modern-english"
RUN curl -O ${BASE_URL}/0.ckpt.h5 \
    && curl -O ${BASE_URL}/0.ckpt.json \
    && curl -O ${BASE_URL}/1.ckpt.h5 \
    && curl -O ${BASE_URL}/1.ckpt.json \
    && curl -O ${BASE_URL}/2.ckpt.h5 \
    && curl -O ${BASE_URL}/2.ckpt.json \
    && curl -O ${BASE_URL}/3.ckpt.h5 \
    && curl -O ${BASE_URL}/3.ckpt.json \
    && curl -O ${BASE_URL}/4.ckpt.h5 \
    && curl -O ${BASE_URL}/4.ckpt.json

ENV CALAMARI_MODEL_CHECKPOINT="4.ckpt.json"

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
