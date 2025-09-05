# Flujo de Uso

```text
Usuario inicia programa
│
├── Pregunta: ¿YouTube o archivo local?
│     ├── YouTube → Solicita URL → Descarga video
│     └── Local   → Solicita ruta al archivo
│
├── Solicita intervalo de captura (segundos o frames)
│
├── Extrae y guarda imágenes en carpeta
│
├── Pregunta: ¿Deseas generar un archivo ZIP?
│     ├── Sí → Crea archivo ZIP
│     └── No → Finaliza
│
└── Fin
```
