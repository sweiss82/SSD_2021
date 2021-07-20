from IAM.admin import UserCreationForm2
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.urls import reverse
# from IAM.models import MyUser, MyUserManager
from django.views.generic import View
from rest import *
# from django.admin import *
from rest.models import Krankenkasse
# from .admin import UserCreationForm2
from rest.models import Rolle


class UserCreationForm2View(View):
    form_class=UserCreationForm2
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(data = request.POST)

        if form.is_valid():
           user = form.save(commit=False)
           benutzername=form.cleaned_data['benutzername']
           password = form.clean_password2()
           benutzerrolle=form.cleaned_data['benutzerrolle']
           user.set_password(password)
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
        password = request.POST.get('passwort', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.benutzerrolle.rolle_bezeichnung == "Arzt":
                return HttpResponseRedirect(reverse('ueberblick_arzt'))
            elif user.benutzerrolle.rolle_bezeichnung == "Patient":
                return HttpResponseRedirect(reverse('ueberblick_patient'))
            else:
                return HttpResponseRedirect(reverse('ueberblick_apotheke'))
        else:
            return render(request, 'Krankenkasse_Login.html', {'error': 'invalidData'})
def logUserIn2(request):
     return render(request, 'Krankenkasse_Login.html')

def logUserOut(request):
    logout(request)
    return render(request, 'LogoutPage.html')

