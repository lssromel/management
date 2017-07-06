# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tasks import *
from django.shortcuts import render, HttpResponse
 
# Create your views here.
def inicio_tarea(request):
    resultado = Procesado_Datos.delay()
    return HttpResponse("Hola su ide de job es : "+str(resultado.id))

