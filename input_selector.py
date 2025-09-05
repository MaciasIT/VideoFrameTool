"""
input_selector.py

Este módulo permite al usuario elegir entre procesar un video desde YouTube o desde un archivo local.
Valida la entrada y retorna la ruta al video que debe procesarse.
"""

import os
from urllib.parse import urlparse

def is_valid_youtube_url(url):
    try:
        parsed = urlparse(url)
        return "youtube.com" in parsed.netloc or "youtu.be" in parsed.netloc
    except:
        return False

def is_valid_file_path(path):
    return os.path.isfile(path) and path.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.webm'))

def get_video_source():
    print("Selecciona el origen del video:")
    print("[1] YouTube")
    print("[2] Archivo local")

    while True:
        choice = input("Ingresa 1 o 2: ").strip()
        if choice == "1":
            url = input("Introduce la URL de YouTube: ").strip()
            if is_valid_youtube_url(url):
                return {"type": "youtube", "value": url}
            else:
                print("❌ URL no válida. Intenta de nuevo.")
        elif choice == "2":
            path = input("Introduce la ruta del archivo de video local: ").strip()
            if is_valid_file_path(path):
                return {"type": "local", "value": path}
            else:
                print("❌ Archivo no válido o no encontrado. Intenta de nuevo.")
        else:
            print("Opción inválida. Elige 1 o 2.")
