# Use an appropriate base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Download Calamari-OCR models
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

# Set an environment variable for the model checkpoint
ENV CALAMARI_MODEL_CHECKPOINT="4.ckpt.json"

# Copy the Flask application
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
