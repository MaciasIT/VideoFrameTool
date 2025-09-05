# Módulo para extraer fotogramas del video
"""
frame_extractor.py

Este módulo permite extraer fotogramas de un video a intervalos definidos
por segundos o por cantidad de frames. Utiliza OpenCV para la lectura del video.
"""

import cv2
import os

def extract_frames(video_path, output_folder, interval=1, by_seconds=True):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"❌ No se pudo abrir el video: {video_path}")
        return 0

    os.makedirs(output_folder, exist_ok=True)

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    print(f"📽️ Video: {video_path}")
    print(f"🎞️ FPS: {fps:.2f}, Duración: {duration:.2f} segundos, Total de frames: {total_frames}")

    saved_frames = 0
    frame_id = 0
    image_id = 0

    interval_frames = int(fps * interval) if by_seconds else interval

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_id % interval_frames == 0:
            filename = os.path.join(output_folder, f"frame_{image_id:05d}.png")
            cv2.imwrite(filename, frame)
            saved_frames += 1
            image_id += 1

        frame_id += 1

    cap.release()
    print(f"✅ {saved_frames} fotogramas guardados en: {output_folder}")
    return saved_frames
