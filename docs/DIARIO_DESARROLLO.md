
## ⚠️ [Limitación Conocida] - Soporte de .webm con OpenCV

**Fecha:** 2025-09-07
**Archivos:** `input_selector.py`, `frame_extractor.py`

**Descripción:**
Aunque `input_selector.py` permite la selección de archivos `.webm` como entrada, se ha identificado que `opencv-python` (utilizado en `frame_extractor.py` para la lectura de videos) puede tener soporte inconsistente o limitado para este formato, dependiendo de la configuración del sistema y los códecs instalados. Esto puede resultar en errores al intentar leer los metadatos del video o al extraer fotogramas, incluso si el archivo `.webm` no está corrupto.

**Recomendación:**
Se recomienda a los usuarios convertir los archivos `.webm` a formatos más ampliamente soportados por OpenCV, como `.mp4` (con códec H.264), antes de procesarlos con la herramienta.

**Resultado:**
Documentación de una limitación conocida para mejorar la experiencia del usuario y proporcionar una solución alternativa.
