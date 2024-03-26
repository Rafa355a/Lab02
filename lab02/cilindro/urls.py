from django.urls import path
from . import views

app_name = 'cilindro'

urlpatterns = [
    path('', views.formulario_cilindro, name='formulario'),
    path('calcular/', views.calcular_volumen, name='calcular'),
]
