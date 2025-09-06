# Flujo de Uso

```text
Usuario inicia programa
│
├── Pregunta: ¿YouTube o archivo local?
│     ├── YouTube → Solicita URL → Descarga video
│     └── Local   → Solicita ruta al archivo
│
├── Solicita intervalo de captura (segundos, frames o minutos)
│
├── Pregunta: ¿Formato de imagen? (PNG, JPG, BMP)
│     └── Si es JPG → Pregunta: ¿Calidad? (Alta, Media, Baja)
│
├── Extrae y guarda imágenes en el formato seleccionado
│
├── Pregunta: ¿Deseas generar un archivo ZIP?
│     ├── Sí → Crea archivo ZIP
│     └── No → Finaliza
│
└── Fin
```
