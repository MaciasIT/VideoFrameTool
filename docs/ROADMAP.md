# Roadmap de Desarrollo - VideoFrameTool

Este roadmap define los pasos implementados y futuros del proyecto de forma estructurada.

---

## ✅ Fase 1: Preparación
- [x] Definir objetivos del proyecto.
- [x] Documentación inicial (`README.md`, `ARCHITECTURE.md`, etc.).
- [x] Crear estructura de carpetas y archivos base.
- [x] Crear `DIARIO_DESARROLLO.md` para registro de tareas.

---

## ✅ Fase 2: Entrada de video
- [x] Crear módulo `input_selector.py` que:
  - [x] Pregunte si el video es de YouTube o archivo local.
  - [x] Valide la entrada (URL válida o ruta existente).
- [x] Implementar pruebas básicas del módulo.

---

## ✅ Fase 3: Descarga de YouTube
- [x] Crear `downloader.py` usando `pytube`.
- [x] Probar con distintos videos (resoluciones, duración, etc.).

---

## ✅ Fase 4: Extracción de fotogramas
- [x] Crear `frame_extractor.py` con OpenCV.
  - [x] Leer el video.
  - [x] Capturar cada N segundos o N frames.
  - [x] Guardar como `.png` en carpeta.

---

## ✅ Fase 5: Generación de ZIP
- [x] Crear `zipper.py` para comprimir la carpeta de imágenes.

---

## ✅ Fase 6: Integración
- [x] Unir todo en `main.py`.
  - [x] Flujo completo de entrada → extracción → ZIP.
- [x] Agregar mensajes en consola y validaciones.

---

## 🔹 Fase 7: Próximas Características

1.  **Formatos de Salida Avanzados:**
    - [ ] Permitir al usuario elegir el formato de imagen de salida (JPG, BMP, etc.).
    - [ ] Añadir opción para configurar la calidad/compresión de la imagen.

2.  **Compatibilidad de Video Ampliada:**
    - [ ] Investigar y añadir soporte para más formatos de video de entrada (MKV, MOV, etc.).

3.  **Selección Inteligente de Fotogramas:**
    - [ ] Implementar un módulo de análisis de imágenes.
    - [ ] Permitir al usuario filtrar y seleccionar fotogramas que contengan principalmente imágenes, gráficos o texto.

4.  **Decisión Estratégica: GUI vs. Funcionalidades:**
    - [ ] Realizar un debate técnico sobre la prioridad entre desarrollar una interfaz gráfica (GUI) o añadir más funcionalidades a la CLI.
    - [ ] Documentar la decisión y los próximos pasos.

---

## 📂 Anexo: Ideas Futuras (v2+)

- Añadir interfaz gráfica (Tkinter, PyQt, o una opción web).
- Subida a servicios en la nube (Google Drive, Dropbox, etc.).
- Integración de IA más avanzada para análisis de contenido de video (detección de objetos, etc.).
- Análisis de audio y extracción de transcripciones.

---

Cada fase se irá registrando paso a paso en `DIARIO_DESARROLLO.md`