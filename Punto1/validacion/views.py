from django.shortcuts import render

# Create your views here.
import csv
from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .forms import cargaArchivo

def subir_archivo(request):
    """
    Vista que muestra el formulario para subir el archivo y procesa la validación.
    """
    mensaje = ""
    errores = []

    if request.method == "POST":
        form = cargaArchivo(request.POST, request.FILES)

        if form.is_valid():
            archivo = request.FILES["archivo"]

            # Se lee el contenido del archivo.
            contenido = archivo.read().decode("utf-8").splitlines()
            

            # csv.reader espera un iterable de líneas y los separa por comas
            reader = csv.reader(contenido)

            for fila_idx, fila in enumerate(reader, start=1):

                # Validacion del  número de columnas = 5
                if len(fila) != 5:
                    errores.append(f"Fila {fila_idx}: debe tener exactamente 5 columnas (encontradas {len(fila)})")
                    continue
                
                #se asigna los valores a su respectuva columna
                col1, col2, col3, col4, col5 = fila

                # Validacion columna 1
                if not col1.isdigit() or not (3 <= len(col1) <= 10):
                    errores.append(f"Fila {fila_idx}, Columna 1: debe ser un número entero con 3 a 10 dígitos")

                # Validacion columna 2
                try:
                    validate_email(col2)
                except ValidationError:
                    errores.append(f"Fila {fila_idx}, Columna 2: email inválido")

                # Validacion columna 3
                if col3 not in ("CC", "TI"):
                    errores.append(f"Fila {fila_idx}, Columna 3: debe ser 'CC' o 'TI'")

                # Validacion columna 4
                try:
                    val = int(col4)
                    if not (500000 <= val <= 1500000):
                        errores.append(f"Fila {fila_idx}, Columna 4: debe estar entre 500000 y 1500000")
                except ValueError:
                    errores.append(f"Fila {fila_idx}, Columna 4: debe ser un número entero")


            if not errores:
                mensaje = "Archivo validado correctamente."

            return render(request, "cargador/resultado.html", {
                "errores": errores,
                "mensaje": mensaje,
            })

    else:
        form = cargaArchivo()

    return render(request, "cargador/subir_archivo.html", {"form": form})