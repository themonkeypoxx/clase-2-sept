from django.contrib import admin
from django.urls import path
from . import views
app_name ="perfil"
urlpatterns = [
    path('perfil/1/', views.perfil_uno, name = 'perfil_uno'),
    path('perfil/2/', views.perfil_dos, name = 'perfil_dos'),
]
