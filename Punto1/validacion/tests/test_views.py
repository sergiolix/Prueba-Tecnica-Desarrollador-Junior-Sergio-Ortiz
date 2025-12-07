from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse


class cargaTests(TestCase):

    def setUp(self):
        self.client = Client()

   #Test 1 Get Mostrar la pagina
    def test_get_carga_archivo(self):
        response = self.client.get(reverse('subir_archivo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cargador/subir_archivo.html')

   # Test 2 Archivo Valido
    def test_archivo_valido(self):
        data = (
            "12345,correo1@example.com,CC,500000,algo\n"
            "98765,correo2b@example.com,TI,600000,algo2\n"
        )

        archivo = SimpleUploadedFile(
            "prueba.csv",
            data.encode('utf-8'),
            content_type="text/csv"
        )

        response = self.client.post(reverse('subir_archivo'), {
            "archivo": archivo
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Archivo validado correctamente")

