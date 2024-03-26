from django.urls import path
from . import views

app_name = 'calcula'

urlpatterns = [
    # ex : /encuesta/
    path('', views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),
]