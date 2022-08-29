from datetime import datetime
from email.policy import HTTP
from this import s
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    return HttpResponse('<h1>Hola Mundo totoooo</h1>') 

def displayDateTime(request):
    dt = datetime.datetime.now()
    s ='<b>Fecha y Hora actual:</b>' +str(dt)
    return HttpResponse(s)

def displayButton(request):
    b = ('<button>Enviar<button>')
    return HttpResponse(b)