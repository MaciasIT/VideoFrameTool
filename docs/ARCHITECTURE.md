# Arquitectura del Proyecto

El proyecto está dividido en varios módulos para mantener el código limpio y escalable.

## 📁 Estructura del proyecto

```
video_frame_extractor/
│
├── main.py                # Flujo principal
├── input_selector.py      # Selección entre YouTube o archivo local
├── downloader.py          # Descarga de YouTube
├── frame_extractor.py     # Extracción y guardado de fotogramas
├── zipper.py              # Creación del archivo ZIP
├── requirements.txt
└── README.md
```

## 🧱 Módulos

- `main.py`: Gestiona la interacción con el usuario.
- `input_selector.py`: Determina si se trata de una URL o un archivo local.
- `downloader.py`: Usa `pytube` para obtener el video.
- `frame_extractor.py`: Usa OpenCV para leer el video y extraer los fotogramas.
- `zipper.py`: Crea un archivo `.zip` con las imágenes.
