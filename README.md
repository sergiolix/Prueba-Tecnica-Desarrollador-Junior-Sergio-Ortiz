# Prueba Desarrollador Junior – Sergio Ortiz

Este repositorio contiene la solución a las dos pruebas solicitadas:
1. **Carga de archivo CSV con Django.**
2. **Script en Python que procesa PDFs, extrae CUFE con regex y almacena en SQLite.**

## Instrucciones para ejecutar el proyecto

### 🔧 Requisitos
- Python 3.10 o superior
- pip instalado


### 📦 Instalación
```bash
pip install -r requirements.txt
```

### 🚀 Ejecutar el proyecto Django
```bash
python manage.py runserver
```

### 🧪 Ejecutar los tests
```bash
python manage.py test
```

### 📄 Script de extracción de CUFE
El script:
- Lee todos los PDFs de una carpeta
- Extrae CUFE usando la regex: `(\b([0-9a-fA-F]\n*){95,100}\b)`
- Guarda en SQLite: nombre de archivo, número de páginas, CUFE y peso del archivo

Ejecución:
```bash
python Extraer_datos.py
```

## 📁 Archivos incluidos
- `requirements.txt` – Librerías necesarias
- `Extraer_datos.py` – Script de extracción
- `README.md` – Este archivo
