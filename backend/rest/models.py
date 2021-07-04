from django.db import models

# Create your models here.
class Medikamentenbestellung(models.Model):
    id = models.AutoField(primary_key=True)
    medikamentenname = models.CharField(max_length=255, unique=False, null=True)
    menge = models.CharField(max_length=50, unique=False, null=True)

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    vorname = models.CharField(max_length=255, unique=False, null=True)
    nachname = models.CharField(max_length=255, unique=False, null=True)
    #geburtsdatum = models.(max_length=255, unique=False, null=True)
    strasse = models.CharField(max_length=255, unique=False, null=True)
    nr = models.CharField(max_length=10, unique=False, null=True)
    plz = models.CharField(max_length=10, unique=False, null=True)
    ort = models.CharField(max_length=10, unique=False, null=True)

class Role(models.Model):
    rolle_bezeichnung=models.CharField(max_length=100)



