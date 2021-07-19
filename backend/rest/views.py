from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import generics

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import UserSerializer
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from icalendar import Calendar, Event
from django.utils.encoding import smart_str
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from wsgiref.util import FileWrapper
from django.http import FileResponse
from django.core import serializers
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

def medikamentBestellen(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            medikamente = Medikament.objects.all()
            apotheken = Apotheke.objects.all()
            return render(request, 'medikamentBestellen.html', {"medikamente": medikamente, 'apotheken': apotheken})
        elif request.method == 'POST':
            patient = Patient.objects.get(username=request.user.benutzername)
            arzt = Arzt.objects.get(id=patient.arzt.id)
            medikamentenbezeichnung = request.POST.get('medikamentenname', None)
            medikament = Medikament.objects.get(medikamentenname = medikamentenbezeichnung)
            dosierung = request.POST.get('dosierung', None)
            menge = request.POST.get('menge', None)
            auswahl = request.POST.get('auswahl', None)
            apothekenname = request.POST.get('apotheke', None)
            apotheke = Apotheke.objects.get(name = apothekenname)
            bestellung = Medikamentenbestellung(medikamentenname = medikament, menge=menge,
            dosierung=dosierung, status=BestellungStatus.OFFEN.value, patient=patient, arzt=arzt, wirdAbgeholt=auswahl,
            apotheke=apotheke)
            bestellung.save()
            return HttpResponseRedirect(reverse('ueberblick_patient'))
        else:
            return HttpResponse("<h2>Ungültige Anfrage!</h2>")
    else:
     return render(request, 'fehlende_Authentifizierung.html' )

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
    if request.user.is_authenticated:
        if request.method == 'GET':
            try:
               arzt = Arzt.objects.get(username = request.user.benutzername)
               medikamentenbestellung = Medikamentenbestellung.objects.filter(arzt=arzt.id, status=BestellungStatus.OFFEN.value)
            except Medikamentenbestellung.DoesNotExist:
               return HttpResponse("<h2>keine Medikamentenbestellung vorhanden!</h2>")
            return render(request, 'medikamentenanfrage_offen.html', {'medikamentenbestellung': medikamentenbestellung})
        elif request.method == 'POST':
            bestellungID = request.POST.get('id', None)
            medikamentenbestellung = Medikamentenbestellung.objects.get(id=bestellungID)
            print("nutzerrolle", request.user.benutzerrolle.rolle_bezeichnung)
            if request.user.benutzerrolle.rolle_bezeichnung == "Arzt":
                try:
                   medikamentenbestellung.bearbeiten(status=BestellungStatus.BESTÄTIGT.value)
                except Medikamentenbestellung.DoesNotExist:
                   return HttpResponse("<h2>Fehler beim Speichern!</h2>")
                return HttpResponseRedirect(reverse('medikamentenanfrageOffen'))
            elif request.user.benutzerrolle.rolle_bezeichnung == "Apotheke":
                try:
                   termin = request.POST.get('termin', None)
                   if medikamentenbestellung.wirdAbgeholt == False:
                        liefertermin = datetime.datetime.strptime(termin, '%d.%m.%Y').date()
                        medikamentenbestellung.bearbeiten(status=BestellungStatus.ARCHIVIERT.value, liefertermin=liefertermin)
                   else:
                        medikamentenbestellung.bearbeiten(status=BestellungStatus.ARCHIVIERT.value)
                except Medikamentenbestellung.DoesNotExist:
                   return HttpResponse("<h2>Fehler beim Speichern!</h2>")
                return HttpResponseRedirect(reverse('ueberblick_apotheke'))
        else:
            return HttpResponse("<h2>Ungültige Anfrage!</h2>")
    else:
        return render(request, 'fehlende_Authentifizierung.html' )

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

def persoenlicheDatenArzt(request):
    if request.method == 'GET':
        return render(request, 'persoenlicheDaten_arzt.html')

def persoenlicheDatenPatient(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
             try:
                 patient = Patient.objects.filter(id=1)
             except patient.DoesNotExist:
                    return HttpResponse("<h2>keine Patient vorhanden!</h2>")
             return render(request, 'persoenlicheDaten_patient.html', {'patient': patient} )

def patientenliste_arzt(request):
        return render(request, 'patientenliste_arzt.html')

def ueberblick_arzt(request):
        if request.user.is_authenticated:
            try:
                arzt = Arzt.objects.get(username=request.user.benutzername)
                patienten = Patient.objects.filter(arzt=arzt)
            except Arzt.DoesNotExist:
                return HttpResponseRedirect(reverse('login'))
            return render(request, 'ueberblick_arzt.html', {'arzt': arzt, 'patienten': patienten})

def ueberblick_patient(request):
        if request.user.is_authenticated:
            try:
                patient = Patient.objects.get(username=request.user.benutzername)
                if patient is None:
                    return HttpResponseRedirect(reverse('login'))
                medikamentenplan_patient = Medikamentenplan.objects.get(patient=patient.id)
                medikamentenplan = Medikamentenplan_Medikamente.objects.filter(medikamentenplan=medikamentenplan_patient.id)
                bestellungen = Medikamentenbestellung.objects.filter(patient=patient)
            except Patient.DoesNotExist:
                return HttpResponseRedirect(reverse('login'))
            return render(request, 'ueberblick_patient.html', {'medikamentenplan': medikamentenplan, 'patient': patient,
                "bestellungen": bestellungen})
        else:
            return render(request, 'fehlende_Authentifizierung.html' )

def ueberblick_apotheke(request):
    if request.user.is_authenticated:
            try:
                apotheke = Apotheke.objects.get(username=request.user.benutzername)
                b_bestätigt = Medikamentenbestellung.objects.filter(apotheke=apotheke.id, status=BestellungStatus.BESTÄTIGT.value)
                b_archiviert = Medikamentenbestellung.objects.filter(apotheke=apotheke.id, status=BestellungStatus.ARCHIVIERT.value)
                bestellungen = list(b_bestätigt) + list(b_archiviert)
            except Apotheke.DoesNotExist:
                return HttpResponse("<h2>keine Bestellungen vorhanden!</h2>")
            return render(request, 'ueberblick_apotheke.html', {'apotheke': apotheke, "bestellungen": bestellungen})
    else:
        return render(request, 'fehlende_Authentifizierung.html' )

def offene_bestellungen_apotheke(request):
        if request.user.is_authenticated:
            try:
                apotheke = Apotheke.objects.get(username = request.user.benutzername)
                b_bestätigt = Medikamentenbestellung.objects.filter(apotheke=apotheke.id, status=BestellungStatus.BESTÄTIGT.value)
                bestellungen = Medikamentenbestellung.objects.filter(apotheke=apotheke.id, status=BestellungStatus.ARCHIVIERT)
                #bestellungen = list(b_bestätigt,b_archiviert)
                print("be",length(bestellungen))
            except Bestellungen.DoesNotExist:
                return HttpResponse("<h2>keine Bestellungen vorhanden!</h2>")
            return render(request, 'offene_bestellungen_apotheke.html', {'bestellungen': bestellungen})
        else:
            return render(request, 'fehlende_Authentifizierung.html' )

def offene_bestellungen_patient(request):
        if request.user.is_authenticated:
            try:
                bestellungen = Medikamentenbestellung.objects.filter(patient=1)
            except bestellungen.DoesNotExist:
                return HttpResponse("<h2>keine Bestellungen vorhanden!</h2>")
            return render(request, 'offene_bestellungen_patient.html', {'bestellungen': bestellungen})
        else:
            return render(request, 'fehlende_Authentifizierung.html' )


def iCalErstellen(request, bestell_id):
        event = Event()
        bestellung = Medikamentenbestellung.objects.get(id=bestell_id)

        event.add('summary', "Liefertermin")
        event.add('dtstart', bestellung.liefertermin)
        event.add('dtend', bestellung.liefertermin)
        beschreibung = "Lieferung des Medikaments " + bestellung.medikamentenname.medikamentenname
        event.add('description', beschreibung)
        event.add('location', 'zu Hause')

        with open('liefertermin.ics', 'wb') as f:
            f.write(event.to_ical())
        f.close()

        response = FileResponse(open('liefertermin.ics', 'rb'))
        return response

def getUserData(request, patient_id):
        patient = Patient.objects.filter(id=patient_id)
        with open("nutzerdaten.txt", "w") as out:
            data = serializers.serialize("json", patient)
            out.write(data)
        out.close()

        response = FileResponse(open('Nutzerdaten.txt', 'rb'))
        response['Content-Disposition'] = 'attachment; filename=Nutzerdaten.json'
        return response

def logout_view(request):
    logout(request)
    return redirect('login')
#todo: persönliche Daten ausgeben verknüpfen -> siehe getUserData()
#def serializejson(obj):
#    serialized_obj = serializers.serialize('json', [ obj, ])
#   return serialized_obj
