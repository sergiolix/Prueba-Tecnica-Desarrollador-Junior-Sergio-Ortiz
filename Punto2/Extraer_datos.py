import os
import re
import sqlite3
from PyPDF2 import PdfReader

#Crea la Base de Datos
conn = sqlite3.connect("facturas.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS facturas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_archivo TEXT,
    numero_paginas INTEGER,
    cufe TEXT,
    peso_archivo FLOAT
)
""")

conn.commit()

#Expresion Regular dada
regex_cufe = r"(\b([0-9a-fA-F]\n*){95,100}\b)"

#RUta de la Carpeta de Las facturas
#ALERTA!!! Cambiar ruta 
ruta_facturas ="C:/Users/Pc/Desktop/facturas"


for archivo in os.listdir(ruta_facturas):
    if archivo.lower().endswith(".pdf"): 
        ruta_completa = os.path.join(ruta_facturas, archivo)

        print(f"\nProcesando: {archivo}")
 
        #se saca el numero de paginas
        try:
            pdf = PdfReader(ruta_completa)
            num_paginas = len(pdf.pages)
        except Exception as e:
            print(f"ERROR leyendo PDF: {e}")
            continue

        #Extrae todo el texto del pdf
        texto = ""
        for pagina in pdf.pages:
            texto += pagina.extract_text() or ""

        #Se saca el CUFE del archivo
        coincidencia = re.search(regex_cufe, texto)

        if coincidencia:
            cufe = coincidencia.group(0).replace("\n", "")
        else:
            cufe = "NO ENCONTRADO"

        #Se saca el peso del archivo
        peso_kb = os.path.getsize(ruta_completa) / 1024

        #Guarda la inforamcion en la base de datos
        cursor.execute("""
            INSERT INTO facturas (nombre_archivo, numero_paginas, cufe, peso_archivo_kb)
            VALUES (?, ?, ?, ?)
        """, (archivo, num_paginas, cufe, peso_kb))

        conn.commit()

        print(f" → Guardado en BD | Páginas: {num_paginas} | Peso: {peso_kb:.2f} KB | CUFE: {cufe[:20]}...")


conn.close()

print("\nProceso terminado.")