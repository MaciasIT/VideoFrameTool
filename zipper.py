"""
zipper.py

Este módulo permite comprimir una carpeta con imágenes en un archivo ZIP.
"""

import os
import zipfile

def zip_folder(folder_path, zip_name=None):
    if not os.path.exists(folder_path):
        print(f"❌ Carpeta no encontrada: {folder_path}")
        return None

    if not zip_name:
        zip_name = folder_path.rstrip("/\\") + ".zip"

    zip_name = os.path.abspath(zip_name)

    print(f"📦 Comprimiendo carpeta: {folder_path}")
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, folder_path)
                zipf.write(full_path, arcname)

    print(f"✅ Archivo ZIP creado: {zip_name}")
    return zip_name
