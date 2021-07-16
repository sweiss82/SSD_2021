from django.db import models
from enum import Enum

# Create your models here.

class Medikament(models.Model):
    id = models.AutoField(primary_key=True)
    medikamentenname = models.CharField(max_length=255, unique=False, null=True)

class Arzt(models.Model):
    id = models.AutoField(primary_key=True)
    vorname = models.CharField(max_length=255, unique=False, null=True)
    nachname = models.CharField(max_length=255, unique=False, null=True)
    #geburtsdatum = models.(max_length=255, unique=False, null=True)
    praxisname = models.CharField(max_length=255, unique=False, null=True)
    strasse = models.CharField(max_length=255, unique=False, null=True)
    nr = models.CharField(max_length=10, unique=False, null=True)
    plz = models.CharField(max_length=10, unique=False, null=True)
    ort = models.CharField(max_length=10, unique=False, null=True)
    username = models.CharField(max_length=255, unique=False, null=True)

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    vorname = models.CharField(max_length=255, unique=False, null=True)
    nachname = models.CharField(max_length=255, unique=False, null=True)
    username = models.CharField(max_length=255, unique=False, null=True)
    #geburtsdatum = models.(max_length=255, unique=False, null=True)
    strasse = models.CharField(max_length=255, unique=False, null=True)
    nr = models.CharField(max_length=10, unique=False, null=True)
    plz = models.CharField(max_length=10, unique=False, null=True)
    ort = models.CharField(max_length=10, unique=False, null=True)
    arzt = models.ForeignKey(Arzt, on_delete=models.CASCADE, null=True)

class Apotheke(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=False, null=True)
    username = models.CharField(max_length=255, unique=False, null=True)
    strasse = models.CharField(max_length=255, unique=False, null=True)
    nr = models.CharField(max_length=10, unique=False, null=True)
    plz = models.CharField(max_length=10, unique=False, null=True)
    ort = models.CharField(max_length=10, unique=False, null=True)

class BestellungStatus(Enum):
    OFFEN = "Offen"
    BESTÄTIGT = "Bestätigt"
    ABGELEHNT = "Abgelehnt"
    ARCHIVIERT = "Archiviert"

class Medikamentenbestellung(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    arzt = models.ForeignKey(Arzt, on_delete=models.CASCADE, null=True)
    apotheke = models.ForeignKey(Apotheke, on_delete=models.CASCADE, null=True)
    medikamentenname = models.ForeignKey(Medikament, on_delete=models.CASCADE, null=True)
    menge = models.CharField(max_length=50, unique=False, null=True)
    dosierung = models.CharField(max_length=50, unique=False, null=True)
    wirdAbgeholt = models.BooleanField(null=True)
    status = models.CharField(max_length=50, unique=False, null=True)
    liefertermin = models.DateField(auto_now=False, null=True)

    def bearbeiten(self, status, *args,  **kwargs):
        self.status = status
        self.liefertermin = kwargs.get('liefertermin', None)
        self.save()

class Medikamentenplan(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    #medikamente = models.ManyToManyField(Medikament, through='Medikamentenplan_Medikamente', null=True) # Ordered list of medikamente
    medikamente = models.ManyToManyField(Medikament, through='Medikamentenplan_Medikamente', null=True) # Ordered list of medikamente

class Medikamentenplan_Medikamente(models.Model):
    id = models.AutoField(primary_key=True)
    medikamentenplan = models.ForeignKey(Medikamentenplan, on_delete=models.CASCADE, null=True)
    medikament = models.ForeignKey(Medikament, on_delete=models.CASCADE, null=True)
    wochentag = models.CharField(max_length=50, unique=False, null=True)
    uhrzeit = models.CharField(max_length=50, unique=False, null=True)
    menge = models.CharField(max_length=50, unique=False, null=True)
    kommentar = models.CharField(max_length=50, unique=False, null=True)

class Krankenkasse(models.Model):
    id = models.AutoField(primary_key=True)
    bezeichnung = models.CharField(max_length=70, unique=False, null=True)

class Rolle(models.Model):
    rolle_bezeichnung=models.CharField(max_length=100)



