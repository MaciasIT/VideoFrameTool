"""
downloader.py

Este módulo descarga un video desde YouTube usando pytube.
Retorna la ruta local al archivo de video descargado.
"""

from pytube import YouTube
import os

def download_youtube_video(url, output_path="downloads"):
    try:
        print(f"🔽 Descargando video desde: {url}")
        yt = YouTube(url)

        # Selecciona la mejor resolución progresiva (video + audio)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

        if not stream:
            print("❌ No se encontró un stream compatible.")
            return None

        os.makedirs(output_path, exist_ok=True)
        downloaded_path = stream.download(output_path=output_path)

        print(f"✅ Video descargado en: {downloaded_path}")
        return downloaded_path

    except Exception as e:
        print(f"❌ Error al descargar el video: {e}")
        return None
