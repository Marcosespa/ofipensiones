from django.shortcuts import render

def inicio(request):
    return render(request, 'ofipensiones/inicio.html')
