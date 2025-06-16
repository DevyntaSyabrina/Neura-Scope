from PIL import Image, ImageDraw, ImageFont
import torch
import numpy as np
import random

# Load model YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def get_color(label):
    random.seed(hash(label) % 10000)  # Konsisten per label
    return tuple(random.choices(range(50, 255), k=3))

def deteksi_objek(img_pil):
    # Konversi ke numpy
    img_np = np.array(img_pil)

    # Deteksi objek
    results = model(img_np)
    deteksi = results.pandas().xyxy[0]

    hasil = []
    img_draw = img_pil.convert("RGB").copy()
    draw = ImageDraw.Draw(img_draw)

    # Font bawaan sistem jika tersedia
    try:
        font = ImageFont.truetype("arial.ttf", 14)
    except:
        font = ImageFont.load_default()

    for _, row in deteksi.iterrows():
        nama = row['name']
        akurasi = round(row['confidence'] * 100, 2)
        hasil.append({
            "nama": nama,
            "akurasi": akurasi
        })

        # Gambar kotak
        x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
        draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
        label = f"{nama} ({akurasi}%)"
        draw.text((x1 + 4, y1 + 4), label, fill="red", font=font)

    return hasil, img_draw
