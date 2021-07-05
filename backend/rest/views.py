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
    else:
        return HttpResponse("<h2>Speichern2 erfolgreich!</h2>")

def medikamentenplanEinsehen(request):
    if request.method == 'GET':
        return render(request, 'medikamentenplan.html', )

def medikamentenplanDetailsEinsehen(request):
    if request.method == 'GET':
        return render(request, 'medikamentenplanDetails.html', )

def medikamentenanfrageOffen(request):
    if request.method == 'GET':
        return render(request, 'medikamentenanfrage_offen.html')

def Einloggen(request):
    if request.method == 'GET':
        print("caled login")
        return render(request, 'Login.html')
    else:
        return render(request, 'Login.html')

def krankenkasseLogin(request):
    if request.method == 'GET':
        return render(request, 'Krankenkasse_Login.html')

def persoenlicheDatenArzt(request):
    if request.method == 'GET':
        return render(request, 'persoenlicheDaten_arzt.html')

def patientenliste_arzt(request):
        return render(request, 'patientenliste_arzt.html')

def ueberblick_arzt(request):
        return render(request, 'ueberblick_arzt.html')

def ueberblick_patient(request):
        return render(request, 'ueberblick_patient.html')

