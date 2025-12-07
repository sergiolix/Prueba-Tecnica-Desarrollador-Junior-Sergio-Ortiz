from django import forms

class cargaArchivo(forms.Form):
    archivo = forms.FileField(
        label="Archivo",
    )