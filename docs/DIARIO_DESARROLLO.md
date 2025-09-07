## ✅ [Fase 14 - Corrección de Errores]

**Fecha:** 2025-09-07
**Archivo:** `frame_extractor.py`

**Descripción:**
Se ha implementado una validación robusta para los metadatos del video (FPS y número total de fotogramas) leídos por OpenCV en `frame_extractor.py`. Anteriormente, valores negativos o erróneos para la duración o el total de fotogramas podían causar errores en tiempo de ejecución. Ahora, si `cv2.CAP_PROP_FPS` o `cv2.CAP_PROP_FRAME_COUNT` retornan valores inválidos (cero o negativos), el programa detectará el problema, informará al usuario y abortará la extracción de fotogramas de manera controlada.

**Resultado:**
Mejora la estabilidad del programa al manejar videos corruptos o con metadatos ilegibles, evitando fallos inesperados y proporcionando retroalimentación clara al usuario.