# Diario de Desarrollo


## ✅ [Fase 1 - Preparación]

**Fecha:** 2025-09-05  
**Descripción:**  
Se ha creado la estructura base del proyecto VideoFrameTool, incluyendo los archivos principales (`main.py`, `input_selector.py`, `downloader.py`, `frame_extractor.py`, `zipper.py`, `requirements.txt`) y la documentación `README.md`.

**Resultado:**  
Proyecto listo para comenzar la fase 2: desarrollo del módulo de entrada de video (`input_selector.py`).

---

## ✅ [Fase 2 - Entrada de video]

**Fecha:** 2025-09-05  
**Archivo:** `input_selector.py`

**Descripción:**  
Se ha implementado el módulo `input_selector.py`, que solicita al usuario el origen del video (YouTube o archivo local), valida la entrada, y retorna un diccionario con la fuente.

**Validaciones:**
- URLs de YouTube (`youtube.com` o `youtu.be`)
- Archivos locales `.mp4`, `.avi`, `.mov`, `.mkv`

**Resultado:**  
El sistema ya puede aceptar entradas de video desde diferentes fuentes.

---

## ✅ [Fase 3 - Descarga de YouTube]

**Fecha:** 2025-09-05  
**Archivo:** `downloader.py`

**Descripción:**  
Se ha creado el módulo `downloader.py` que permite descargar videos de YouTube utilizando la librería `pytube`. El módulo selecciona automáticamente el mejor stream progresivo en formato `.mp4` y lo guarda en una carpeta `downloads/`.

**Validaciones:**
- Verifica disponibilidad de stream compatible.
- Captura errores durante la descarga.

**Resultado:**  
El programa puede descargar videos desde YouTube y usarlos como entrada para el análisis.

---

## ✅ [Fase 4 - Extracción de fotogramas]

**Fecha:** 2025-09-05  
**Archivo:** `frame_extractor.py`

**Descripción:**  
Se implementó el módulo `frame_extractor.py` que permite extraer fotogramas desde un video usando OpenCV. Los fotogramas se guardan como imágenes `.png` numeradas secuencialmente.

**Características:**
- Permite intervalos por segundos o por número de frames.
- Muestra estadísticas del video: FPS, duración, número total de frames.

- Guarda los fotogramas en una carpeta específica.

**Resultado:**  
El sistema puede generar imágenes a partir del contenido del video de forma flexible y controlada.

---

## ✅ [Fase 5 - Generación de ZIP]

**Fecha:** 2025-09-05  
**Archivo:** `zipper.py`

**Descripción:**  
Se ha desarrollado el módulo `zipper.py`, encargado de comprimir una carpeta (por ejemplo, la de imágenes extraídas) en un archivo `.zip`.

**Características:**
- Comprime todos los archivos manteniendo la estructura relativa.
- Usa el módulo estándar `zipfile`.
- Retorna la ruta absoluta del `.zip` generado.

**Resultado:**  
El sistema puede empaquetar fácilmente los resultados en un archivo comprimido, ideal para compartir o archivar.

---

## ✅ [Fase 6 - Integración del sistema]

**Fecha:** 2025-09-05  
**Archivo:** `main.py`

**Descripción:**  
Se ha desarrollado el script `main.py` que conecta todos los módulos del sistema en un flujo funcional:

1. Entrada del usuario (YouTube o archivo local)
2. Descarga (si es necesario)
3. Selección de intervalo de extracción
4. Extracción de fotogramas
5. Opción de generar archivo ZIP

**Resultado:**  
El sistema completo ya es funcional desde la consola, listo para ser probado de extremo a extremo.

---

## ✅ [Fase 7 - Tests automatizados: input_selector]

**Fecha:** 2025-09-05  
**Archivo:** `tests/test_input_selector.py`

**Descripción:**  
Se ha creado el primer test automatizado del proyecto, utilizando `unittest`.

**Cobertura:**
- Validación de URLs de YouTube
- Validación de archivos locales
- Simulación de entrada del usuario con `unittest.mock`

**Resultado:**  
El módulo `input_selector.py` está cubierto por pruebas unitarias automáticas.

---

## ✅ [Fase 7 - Tests automatizados: zipper]

**Fecha:** 2025-09-05  
**Archivo:** `tests/test_zipper.py`

**Descripción:**  
Se ha desarrollado un test unitario para el módulo `zipper.py`, verificando su capacidad de comprimir correctamente una carpeta de archivos.

**Cobertura:**
- Crea archivos de prueba en una carpeta temporal.
- Ejecuta compresión con `zip_folder()`.
- Verifica la existencia y el contenido del archivo `.zip`.

**Resultado:**  
El módulo `zipper.py` está cubierto por pruebas unitarias automáticas.

---

## ✅ [Fase 7 - Tests automatizados: frame_extractor]

**Fecha:** 2025-09-05  
**Archivo:** `tests/test_frame_extractor.py`

**Descripción:**  
Se ha creado un test automatizado para el módulo `frame_extractor.py`. Utiliza un video artificial generado dinámicamente para probar la extracción de fotogramas.

**Cobertura:**
- Extracción por segundos (`by_seconds=True`)
- Extracción por número de frames (`by_seconds=False`)
- Verificación del número de imágenes generadas

**Resultado:**  
El módulo `frame_extractor.py` está cubierto por pruebas unitarias automáticas y reproduce condiciones reales de uso.

---

## ✅ [Fase 8 - Métodos de distribución]

**Fecha:** 2025-09-05  
**Archivos:**
- `dist_zip/VideoFrameTool.zip`
- `dist_zip/README.md`
- `dist_setup/setup.py`
- `dist_setup/README.md`

**Descripción:**  
Se han implementado dos métodos de distribución para el proyecto:

### 📦 Método 1: ZIP
- Permite compartir fácilmente el proyecto comprimido.
- Contiene instrucciones para descomprimir, instalar dependencias y ejecutar el programa.

### 🛠️ Método 2: setup.py
- Permite instalar el proyecto como un paquete Python estándar usando `pip install .`.
- Incluye entry point para ejecutar desde consola (`video-frame-tool`).

**Resultado:**  
El proyecto está listo para ser compartido y utilizado tanto de forma manual como profesional.

---

## ✅ [Fase 9 - Correcciones y Mejoras]

**Fecha:** 2025-09-05  
**Archivo:** `input_selector.py`

**Descripción:**  
Se ha corregido el módulo `input_selector.py` para incluir la extensión `.webm` como formato de video local válido. Anteriormente, solo se aceptaban `.mp4`, `.avi`, `.mov` y `.mkv`.

**Resultado:**  
El sistema ahora puede procesar archivos de video con extensión `.webm` desde el origen local.

---

## ✅ [Fase 9 - Correcciones y Mejoras]

**Fecha:** 2025-09-05  
**Archivo:** `downloader.py` (y `pytube` librería externa)

**Descripción:**  
Se ha investigado el problema de descarga de videos de YouTube. Aunque la versión de `pytube` instalada (`15.0.0`) es la más reciente, se ha realizado una reinstalación forzada (`pip install --upgrade --force-reinstall pytube`) para asegurar una instalación limpia y mitigar posibles problemas de parsing debido a los frecuentes cambios en la API de YouTube.

**Resultado:**  
Se ha aplicado una solución común para problemas intermitentes de `pytube`. Se recomienda al usuario probar la descarga de videos nuevamente. Se documenta que los problemas con `pytube` pueden ser recurrentes debido a la naturaleza cambiante de la API de YouTube.

---

## ✅ [Fase 9 - Correcciones y Mejoras]

**Fecha:** 2025-09-05  
**Archivo:** `main.py`

**Descripción:**  
Se ha modificado el script principal (`main.py`) para cambiar el formato del nombre del archivo ZIP generado. Ahora, el nombre sigue el patrón `CapturasPNG_Total[numero de capturas].zip`, donde `[numero de capturas]` es la cantidad de fotogramas extraídos.

**Resultado:**  
El archivo ZIP de salida tiene un nombre más descriptivo y útil para el usuario, incluyendo el total de capturas.

---

## ✅ [Fase 10 - Nuevas Funcionalidades]

**Fecha:** 2025-09-05  
**Archivo:** `main.py`

**Descripción:**  
Se ha añadido una nueva opción en el script principal (`main.py`) para permitir al usuario especificar el intervalo de extracción de fotogramas en minutos. Si se selecciona esta opción, el valor en minutos se convierte automáticamente a segundos antes de ser procesado por el módulo `frame_extractor.py`.

**Resultado:**  
El usuario ahora tiene mayor flexibilidad para definir los intervalos de extracción, especialmente útil para videos de larga duración.

---

## ✅ [Fase 11 - Nuevas Funcionalidades]

**Fecha:** 2025-09-06  
**Archivo:** `frame_extractor.py`

**Descripción:**  
Se ha implementado la funcionalidad para permitir al usuario seleccionar el formato de imagen de salida para los fotogramas extraídos, incluyendo `.png`, `.jpg` y `.bmp`.

**Resultado:**  
El usuario tiene mayor control sobre el formato de las imágenes de salida.

---

## ✅ [Fase 12 - Nuevas Funcionalidades]

**Fecha:** 2025-09-06  
**Archivo:** `frame_extractor.py`

**Descripción:**  
Se ha añadido la opción de ajustar la calidad de las imágenes para el formato JPG (Alta, Media, Baja) durante la extracción de fotogramas.

**Resultado:**  
El usuario puede optimizar el tamaño y la calidad de las imágenes JPG generadas.

---

## ✅ [Fase 13 - Extracción de fotogramas con OCR]

**Fecha:** 2025-09-06  
**Archivos:** `frame_extractor.py`, `main.py`

**Descripción:**  
Se ha implementado la funcionalidad de extracción de fotogramas con detección de texto (OCR). El módulo `frame_extractor.py` ahora incluye una función `has_text()` que utiliza `pytesseract` para identificar si un fotograma contiene texto. El script principal `main.py` expone una nueva opción al usuario (`only_text_frames`) para activar esta funcionalidad, permitiendo guardar solo aquellos fotogramas que contengan texto.

**Resultado:**  
El usuario puede realizar una extracción más selectiva de fotogramas, enfocándose únicamente en aquellos con contenido textual, lo que es útil para análisis de documentos o presentaciones en video.

