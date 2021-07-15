from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import generics

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import UserSerializer
import datetime
from django.shortcuts import HttpResponse
from rest.models import BestellungStatus
# Create your views here.

def medikamentBestellen(request):
    if request.method == 'GET':
        return render(request, 'medikamentBestellen.html')
    elif request.method == 'POST':
        medikamentenbezeichnung = request.POST.get('bestellung_medi', None)
        menge = request.POST.get('bestellung_menge', None)
        dosis = request.POST.get('bestellung_dosis', None)
        arzt = Arzt.objects.get(id=1)
        patient = Patient.objects.get(id=1)
        date = datetime.datetime(2001,1,1,8,30) #todo: datum bei apo auswählen
        bestellung = Medikamentenbestellung(patient=patient, medikamentenname=Medikament.objects.get(medikamentenname=medikamentenbezeichnung), menge=menge, dosis=dosis, status=BestellungStatus.OFFEN, arzt=arzt, datum=date)
        bestellung.save()
        return HttpResponse("<h2>Speichern erfolgreich!</h2>")
    else:
        return HttpResponse("<h2>Speichern2 erfolgreich!</h2>")

def medikamentenplanEinsehen(request):
    user_id=123
    if request.method == 'GET':
        try:
            medikamentenplan = Medikamentenplan.objects.get(patient=1)
            return render(request, 'medikamentenplan.html', {'medikamentenplan': medikamentenplan} )
        except Medikamentenplan.DoesNotExist:
            return HttpResponse("<h2>keine Medikamentenplan vorhanden!</h2>")

def medikamentenplanDetailsEinsehen(request):
    if request.method == 'GET':
        return render(request, 'medikamentenplanDetails.html', )

def medikamentenanfrageOffen(request):
    if request.method == 'GET':
         try:
            medikamentenbestellung = Medikamentenbestellung.objects.filter(arzt=1)
         except Medikamentenbestellung.DoesNotExist:
            return HttpResponse("<h2>keine Medikamentenbestellung vorhanden!</h2>")
         return render(request, 'medikamentenanfrage_offen.html', {'medikamentenbestellung': medikamentenbestellung})

def Einloggen(request):
    if request.method == 'GET':
        try:
            krankenkassen = Krankenkasse.objects.all()
        except Krankenkasse.DoesNotExist:
            return HttpResponse("<h2>keine Krankenkasse vorhanden!</h2>")
        return render(request, 'Login.html', {'krankenkassen': krankenkassen})
    else:
        return render(request, 'Login.html')

def krankenkasseLogin(request):
    if request.method == 'GET':
        return render(request, 'Krankenkasse_Login.html')
    else:
         return render(request, 'Krankenkasse_Login.html')

#todo: wann wird das aufgerufen?
def persoenlicheDatenArzt(request):
    if request.method == 'GET':
        return render(request, 'persoenlicheDaten_arzt.html')

def persoenlicheDatenPatient(request):
    if request.method == 'GET':
         try:
             patient = Patient.objects.filter(id=1)
         except patient.DoesNotExist:
                return HttpResponse("<h2>keine Patient vorhanden!</h2>")
         return render(request, 'persoenlicheDaten_patient.html', {'patient': patient} )

def patientenliste_arzt(request):
        return render(request, 'patientenliste_arzt.html')

def ueberblick_arzt(request):
        try:
            arzt = Arzt.objects.get(id=1)
            patientenliste = Patient.objects.all()
        except arzt.DoesNotExist:
            return HttpResponse("<h2>keine Arzt vorhanden!</h2>")
        return render(request, 'ueberblick_arzt.html', {'arzt': arzt, 'patient': patientenliste})

def ueberblick_patient(request):
        if request.user.is_authenticated:
            try:
                patient = Patient.objects.get(username=request.user.benutzername)
                medikamentenplan = Medikamentenplan.objects.prefetch_related('Medikamentenplan_Medikamente').get(patient=patient.id)
            except Medikamentenplan.DoesNotExist:
                return HttpResponse("<h2>keine Medikamentenplan vorhanden!</h2>")
            #try:
            #    patient = Patient.objects.get(id=3)
            #    patienten = Patient.objects.all()
            #    bestellungen = Medikamentenbestellung.objects.filter(patient=1)
           # except patient.DoesNotExist:
            #       return HttpResponse("<h2>keine Patient vorhanden!</h2>")
            return render(request, 'ueberblick_patient.html', {'medikamentenplan': medikamentenplan, 'patient': patient})

def offene_bestellungen_patient(request):
        try:
            bestellungen = Medikamentenbestellung.objects.filter(patient=1)
        except bestellungen.DoesNotExist:
            return HttpResponse("<h2>keine Bestellungen vorhanden!</h2>")
        return render(request, 'offene_bestellungen_patient.html', {'bestellungen': bestellungen})

#todo: persönliche Daten ausgeben verknüpfen
def serializejson(obj):
    serialized_obj = serializers.serialize('json', [ obj, ])
    return serialized_obj
