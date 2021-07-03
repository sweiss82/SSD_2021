from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import generics

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import UserSerializer
from django.shortcuts import HttpResponse

# Create your views here.

def medikamentBestellen(request):
    if request.method == 'GET':
        return render(request, 'medikamentBestellen.html')
    elif request.method == 'POST':
        medikamentenbezeichnung = request.POST.get('medikamentenbezeichnung', None)
        menge = request.POST.get('menge', None)
        bestellung = Medikamentenbestellung(medikamentenname = medikamentenbezeichnung, menge=menge)
        bestellung.save()
        return HttpResponse("<h2>Speichern erfolgreich!</h2>")

def medikamentenplanEinsehen(request):
    if request.method == 'GET':
        return render(request, 'medikamentenplan.html', )

def medikamentenplanDetailsEinsehen(request):
    if request.method == 'GET':
        return render(request, 'medikamentenplanDetails.html', )

def medikamentenanfrageOffen(request):
    if request.method == 'GET':
        return render(request, 'medikamentenanfrage_offen.html')
