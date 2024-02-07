import requests
import streamlit as st
import cv2
from PIL import Image
import numpy as np
import os
from ultralytics import YOLO
import io

ocr_port = os.getenv("ocr_port", "5000")
model_path = os.getenv("model_path")
ip_or_service_addres = os.getenv("ip_or_service_addres",'127.0.0.1')

if model_path is None:
    st.error("Nie znaleziono ścieżki modelu. Ustaw zmienną środowiskową 'model_path'.")
    st.stop()


model = YOLO(model_path)
url = f"http://{ip_or_service_addres}:{ocr_port}/ocr"


def send_image_for_ocr(image, image_name):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    image_bytes = buffered.getvalue()

    files = {"file": (image_name, image_bytes, "image/jpeg")}
    response = requests.post(url, files=files)
    return response.json()  # Zwróć odpowiedź JSON


def predict(image):
    im = np.array(image)
    im_g = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    im_g = cv2.cvtColor(im_g, cv2.COLOR_GRAY2RGB)

    pred = model.predict(im_g)[0]
    im_res = im.copy()
    res = []
    for i, (x1, y1, x2, y2, prob, _) in enumerate(pred.boxes.data):
        im_part = Image.fromarray(im[int(y1) : int(y2), int(x1) : int(x2)])
        im_name = f"{i+1}_box.jpg"
        ocr_response = send_image_for_ocr(image=im_part, image_name=im_name)
        im_res = cv2.rectangle(
            im_res, (int(x1), int(y1)), (int(x2), int(y2)), color=(255, 0, 0), thickness=5
        )
        res.append((ocr_response.get("text", ""), im_part))
    return res, im_res


st.title("Detekcja obiektów z YOLO")
uploaded_file = st.file_uploader("Prześlij obraz", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Przesłany obraz", use_column_width=True)
    st.write("Przetwarzanie...")
    result, predicted_image_arr = predict(image)
    st.image(Image.fromarray(predicted_image_arr),caption='Oznaczone dokumenty')
    for i,(r_text,r_im_ar) in enumerate(result):
        st.text(r_text)
        st.image(r_im_ar,caption=f'wykryty_obiekt_{i+1}')
