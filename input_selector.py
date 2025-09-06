"""
input_selector.py

Este módulo permite al usuario elegir entre procesar un video desde YouTube o desde un archivo local.
Valida la entrada y retorna la ruta al video que debe procesarse.
"""

import os
from urllib.parse import urlparse

# Lista de formatos de video soportados para facilitar mantenimiento
SUPPORTED_VIDEO_FORMATS = ('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.webm')

def is_valid_youtube_url(url):
    """Verifica si una URL es de YouTube."""
    try:
        parsed = urlparse(url)
        return "youtube.com" in parsed.netloc or "youtu.be" in parsed.netloc
    except:
        return False

def get_video_source():
    """
    Pregunta al usuario por el origen del video (YouTube o local) y valida la entrada.

    Returns:
        dict: Un diccionario con el tipo de fuente ('youtube' or 'local') y el valor (URL o ruta).
    """
    print("\nSelecciona el origen del video:")
    print("[1] YouTube")
    print("[2] Archivo local")

    while True:
        choice = input("Ingresa 1 o 2: ").strip()
        if choice == "1":
            url = input("Introduce la URL de YouTube: ").strip()
            if is_valid_youtube_url(url):
                return {"type": "youtube", "value": url}
            else:
                print("❌ URL de YouTube no válida. Intenta de nuevo.")
        
        elif choice == "2":
            path = input("Introduce la ruta del archivo de video local: ").strip().strip('"') # Limpia comillas
            
            # 1. Verificar si el archivo existe
            if not os.path.isfile(path):
                print(f"❌ Error: El archivo no se encuentra en la ruta especificada: {path}")
                continue # Vuelve a pedir la ruta

            # 2. Verificar si la extensión es de un formato soportado
            file_extension = os.path.splitext(path)[1].lower()
            if file_extension not in SUPPORTED_VIDEO_FORMATS:
                print(f"❌ Error: El formato de archivo '{file_extension}' no está soportado.")
                print(f"   Formatos soportados: {', '.join(SUPPORTED_VIDEO_FORMATS)})")
                continue # Vuelve a pedir la ruta
            
            # Si ambas validaciones pasan, es una ruta válida
            return {"type": "local", "value": path}

        else:
            print("Opción inválida. Elige 1 o 2.")
