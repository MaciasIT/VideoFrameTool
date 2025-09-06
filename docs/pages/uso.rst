Uso
===

Para utilizar VideoFrameTool, sigue los siguientes pasos:

1.  **Ejecutar la aplicación:**

    Abre tu terminal o línea de comandos, navega hasta el directorio raíz del proyecto y ejecuta el script principal:

    .. code-block:: bash

       python main.py

2.  **Seleccionar la fuente del video:**

    La aplicación te preguntará si deseas procesar un video de YouTube o un archivo local. Sigue las instrucciones en pantalla para proporcionar la URL o la ruta del archivo.

3.  **Elegir el método de extracción de fotogramas:**

    Podrás seleccionar cómo deseas que se extraigan los fotogramas:

    *   **Cada N segundos:** Extrae un fotograma cada cierto número de segundos.
    *   **Cada N fotogramas:** Extrae un fotograma cada cierto número de fotogramas.
    *   **Cada N minutos:** Extrae un fotograma cada cierto número de minutos.

    Deberás introducir el valor numérico para el intervalo seleccionado.

4.  **Seleccionar el formato de imagen de salida:**

    Elige entre los siguientes formatos para los fotogramas extraídos:

    *   **PNG:** Formato sin pérdida, ideal para alta calidad pero con archivos más grandes.
    *   **JPG:** Formato con compresión, resultando en archivos más pequeños.
    *   **BMP:** Formato sin compresión, genera archivos muy grandes.

    Si seleccionas JPG, se te pedirá que elijas un nivel de calidad (Alta, Media, Baja).

5.  **Opción de extracción de fotogramas con texto (OCR):**

    Se te preguntará si deseas extraer *solo* los fotogramas que contengan texto. Si respondes 's' (sí), la herramienta utilizará Tesseract OCR para analizar cada fotograma y solo guardará aquellos en los que detecte texto. Si respondes 'n' (no), se guardarán los fotogramas según el intervalo especificado, sin realizar detección de texto.

    .. note::
        Para que la detección de texto funcione correctamente, debes tener `Tesseract OCR` instalado en tu sistema y configurado en el PATH. Puedes descargarlo desde `https://tesseract-ocr.github.io/tessdoc/Installation.html`.

6.  **Comprimir los fotogramas en un archivo ZIP (opcional):**

    Al finalizar la extracción, la aplicación te preguntará si deseas crear un archivo ZIP con todos los fotogramas guardados. Si confirmas, se generará un archivo ZIP en el directorio de salida.

7.  **Ubicación de los fotogramas:**

    Los fotogramas se guardarán en una carpeta única dentro del directorio `frames/` del proyecto. Si creaste un ZIP, también se te indicará la ruta del archivo ZIP.


Ejecución de Tests
------------------

Para ejecutar los tests del proyecto, utiliza el siguiente comando desde el directorio raíz:

.. code-block:: bash

   python tests/run_tests.py