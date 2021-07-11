from django.shortcuts import render

from django.shortcuts import render
from rest import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from IAM.admin import UserCreationForm2
#from IAM.models import MyUser, MyUserManager
from rest import templates
import rest
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import View
#from .admin import UserCreationForm2
from django.shortcuts import HttpResponse
from rest.models import Rolle
from rest.models import Patient, Arzt, Rolle
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest.models import Patient, Arzt, Rolle
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
#from django.admin import *
import datetime
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class UserCreationForm2View(View):
    form_class=UserCreationForm2
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class(None)
        print("Formulardaten", form)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
           user = form.save(commit=False)
           benutzername=form.cleaned_data['benutzername']
           password = form.clean_password2()
           benutzerrolle=form.cleaned_data['benutzerrolle']
           user.set_password(password)
           user.benutzerrolle = Rolle.objects.get(pk=benutzerrolle)
           user.save()
           return render(request, 'register_response.html', {'message': 'Registrierung erfolgreich!',})
        else:
            return render(request, 'register_response.html', {'message': 'Registrierung nicht erfolgreich!', 'error':'invalid data'})

def logUserIn(request):
    if request.method == 'GET':
        return render(request, 'Login.html')
    if request.method == 'POST':
        username = request.POST.get('mitgliederkennung', None)
        password = request.POST.get('passwort', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('show BAs'))
        else:
            return render(request, 'LoginPage.html', {'error' : 'invalidData',})
def logUserIn2(request):
      return render(request, 'Krankenkasse_Login.html', {'error' : 'invalidData',})

def logUserOut(request):
    logout(request)
    return render(request, 'LogoutPage.html')

