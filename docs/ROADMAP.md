# Roadmap de Desarrollo - VideoFrameTool

Este roadmap define los pasos para implementar el proyecto de forma estructurada y profesional.

---

## 🔹 Fase 1: Preparación
- [x] Definir objetivos del proyecto
- [x] Documentación inicial (`README.md`, `ARCHITECTURE.md`, etc.)
- [x] Crear estructura de carpetas y archivos base
- [x] Crear `DIARIO_DESARROLLO.md` para registro de tareas

---

## 🔹 Fase 2: Entrada de video
- [ ] Crear módulo `input_selector.py` que:
  - Pregunte si el video es de YouTube o archivo local
  - Valide la entrada (URL válida o ruta existente)
- [ ] Implementar pruebas básicas del módulo

---

## 🔹 Fase 3: Descarga de YouTube (opcional)
- [ ] Crear `downloader.py` usando `pytube`
- [ ] Probar con distintos videos (resoluciones, duración, etc.)

---

## 🔹 Fase 4: Extracción de fotogramas
- [ ] Crear `frame_extractor.py` con OpenCV
  - Leer el video
  - Capturar cada N segundos o N frames
  - Guardar como `.png` en carpeta

---

## 🔹 Fase 5: Generación de ZIP
- [ ] Crear `zipper.py` para comprimir la carpeta de imágenes

---

## 🔹 Fase 6: Integración
- [ ] Unir todo en `main.py`
  - Flujo completo de entrada → extracción → ZIP
- [ ] Agregar mensajes en consola y validaciones

---

## 🔹 Fase 7: Mejoras futuras (v2+)
- [ ] Añadir interfaz gráfica (Tkinter o PyQt)
- [ ] Soporte para más formatos de imagen
- [ ] Subida a nube (Google Drive, Dropbox, etc.)
- [ ] Análisis de imágenes (IA, OCR, etc.)

---

Cada fase se irá registrando paso a paso en `DIARIO_DESARROLLO.md`
