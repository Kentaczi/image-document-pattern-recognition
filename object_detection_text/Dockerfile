FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV model_path yolov8n_synth_docs.pt
ENV STREAMLIT_SERVER_PORT 8501
ENV ip_or_service_addres ocr-service

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
