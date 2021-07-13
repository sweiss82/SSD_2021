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
from rest.models import Krankenkasse

class UserCreationForm2View(View):
    form_class=UserCreationForm2
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class(None)
        #print("Formulardaten", form)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(data = request.POST)
        print("form errors", form.errors)
        if form.is_valid():
           user = form.save(commit=False)
           benutzername=form.cleaned_data['benutzername']
           password = form.clean_password2()
           benutzerrolle=form.cleaned_data['benutzerrolle']
           user.set_password(password)
           print("passwort", password)
           print("benutzerrolle", benutzerrolle)
           user.benutzerrolle = Rolle.objects.get(pk=benutzerrolle)
           user.save()
           return HttpResponse("<h2>Registrierung erfolgreich!</h2>")
        else:
           from django.contrib.auth import get_user_model
           User = get_user_model()
           users = User.objects.all()
           return render(request, 'register_response.html', {'users': len(users)})

def logUserIn(request):
    if request.method == 'GET':
        krankenkassen = Krankenkasse.objects.all()
        return render(request, 'Login.html', {'krankenkassen': krankenkassen})
    if request.method == 'POST':
        username = request.POST.get('mitgliederkennung', None)
        print("mitglied", username)
        password = request.POST.get('passwort', None)
        print("pw", password)
        user = authenticate(request, username=username, password=password)
        print("User", user)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('ueberblick_patient'))
        else:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            users = User.objects.all()
            return render(request, 'register_response.html', {'users': users})
             #return HttpResponse("<h2>Credentials invalid!</h2>")
            #eturn render(request, 'LoginPage.html', {'error' : 'invalidData',})
def logUserIn2(request):
     return render(request, 'Krankenkasse_Login.html')

def logUserOut(request):
    logout(request)
    return render(request, 'LogoutPage.html')

