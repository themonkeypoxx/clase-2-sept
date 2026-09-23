from django.shortcuts import render

# Create your views here.}
def perfil_uno(request):
    data= {"nombre":"Mario","año":1980,"correo":"mario.armario@gmail.com"}
    return render(request, 'perfil/p1.html', data)

def perfil_dos(request):
    data= {"nombre":"Ronaldinho","año":1980,"correo":"ronal.dinho@tren.chuchu","foto":"tren.jpg"}
    return render(request, 'perfil/p2.html', data)