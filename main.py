"""
main.py

Script principal que orquesta el funcionamiento del programa VideoFrameTool.
"""

from input_selector import get_video_source
from downloader import download_youtube_video
from frame_extractor import extract_frames
from zipper import zip_folder

import os
import uuid

def main():
    print("🎬 Bienvenido a VideoFrameTool")

    source_info = get_video_source()

    if source_info["type"] == "youtube":
        video_path = download_youtube_video(source_info["value"])
        if not video_path:
            print("❌ No se pudo descargar el video. Saliendo...")
            return
    else:
        video_path = source_info["value"]

    # Crear carpeta de salida única
    session_id = uuid.uuid4().hex[:8]
    output_folder = os.path.join("frames", f"frames_{session_id}")

    # Solicitar método de extracción
    print("\nSelecciona el método de extracción:")
    print("[1] Cada N segundos")
    print("[2] Cada N fotogramas")
    print("[3] Cada N minutos") # New option
    while True:
        choice = input("Opción (1, 2 o 3): ").strip() # Updated prompt
        if choice in ["1", "2", "3"]:
            break
        print("Opción inválida. Intenta de nuevo.")

    by_seconds = (choice == "1" or choice == "3") # If choice is 1 or 3, it's by seconds (after conversion for minutes)

    while True:
        try:
            interval = float(input("Intervalo (número): "))
            if interval > 0:
                break
            else:
                print("Debe ser mayor que 0.")
        except ValueError:
            print("Entrada inválida. Intenta con un número.")

    if choice == "3": # If minutes, convert to seconds
        interval *= 60
        print(f"Intervalo convertido a {interval} segundos.") # Optional: inform user

    # --- Selección de Formato y Calidad ---
    print("\nSelecciona el formato de imagen de salida:")
    print("[1] PNG (sin pérdida, archivo grande)")
    print("[2] JPG (con compresión, archivo pequeño)")
    print("[3] BMP (sin compresión, archivo muy grande)")
    
    format_map = {"1": ".png", "2": ".jpg", "3": ".bmp"}
    while True:
        format_choice = input("Opción (1, 2 o 3): ").strip()
        if format_choice in format_map:
            image_format = format_map[format_choice]
            break
        print("Opción inválida. Intenta de nuevo.")

    quality = 95 # Valor por defecto
    if image_format == ".jpg":
        print("\nSelecciona la calidad de la imagen JPG:")
        print("[1] Alta (mejor calidad, archivo más grande)")
        print("[2] Media (equilibrio calidad/tamaño)")
        print("[3] Baja (peor calidad, archivo más pequeño)")
        
        quality_map = {"1": 95, "2": 85, "3": 50}
        while True:
            quality_choice = input("Opción (1, 2 o 3): ").strip()
            if quality_choice in quality_map:
                quality = quality_map[quality_choice]
                break
            print("Opción inválida. Intenta de nuevo.")

    # --- Nueva opción: Extraer solo frames con texto ---
    only_text_frames = False
    while True:
        text_frame_choice = input("\n¿Deseas extraer solo fotogramas que contengan texto? (s/n): ").strip().lower()
        if text_frame_choice in ["s", "n"]:
            only_text_frames = (text_frame_choice == "s")
            break
        print("Opción inválida. Por favor, responde 's' o 'n'.")

    # --- Extracción de Frames ---
    extracted = extract_frames(
        video_path,
        output_folder,
        interval=interval,
        by_seconds=by_seconds,
        image_format=image_format,
        quality=quality,
        only_text_frames=only_text_frames
    )
    if extracted == 0:
        print("❌ No se extrajo ningún fotograma. Saliendo...")
        return

    # Preguntar si se quiere zip
    choice = input("\n¿Deseas crear un archivo ZIP con las imágenes? (s/n): ").strip().lower()
    if choice == "s":
        # Construir el nombre del archivo ZIP con el nuevo formato
        zip_file_name = f"CapturasPNG_Total{extracted}.zip"
        zip_path = zip_folder(output_folder, zip_name=os.path.join(os.path.dirname(output_folder), zip_file_name))
        if zip_path:
            print(f"🎁 ZIP creado en: {zip_path}")
        else:
            print("❌ No se pudo crear el archivo ZIP.")
    else:
        print("🗂️ Las imágenes han quedado guardadas en la carpeta:", output_folder)

    print("\n✅ Proceso completado.")

if __name__ == "__main__":
    main()
