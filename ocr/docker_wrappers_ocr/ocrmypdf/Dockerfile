FROM python:3.8-slim

WORKDIR /usr/src/app

# Install OCRmyPDF and its dependencies
RUN apt-get update && apt-get install -y \
    ocrmypdf \
    pdfgrep \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
