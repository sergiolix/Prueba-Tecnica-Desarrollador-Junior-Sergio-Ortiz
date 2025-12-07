from django.urls import path
from . import views
urlpatterns = [
    path('', views.subir_archivo, name='subir_archivo'),
]