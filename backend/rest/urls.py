from django.conf.urls import url
from . import views
from django.urls import path
import IAM.views

urlpatterns = [
    path('medikamentenbestellung/', views.medikamentBestellen, name='medikament bestellen'),
    path('medikamentenplan/', views.medikamentenplanEinsehen, name='medikamentenplan'),
    path('medikamentenplanDetails/', views.medikamentenplanDetailsEinsehen, name='medikamentenplanDetails'),
    path('medikamentenanfrageOffen/', views.medikamentenanfrageOffen, name='medikamentenanfrageOffen'),
    path('login/', IAM.views.logUserIn, name='login'),
    path('krankenkasseLogin/', IAM.views.logUserIn2, name='krankenkasseLogin'),
    path('arzt_ueberblick/', views.ueberblick_arzt, name='ueberblick_arzt'),
    path('patient_ueberblick/', views.ueberblick_patient, name='ueberblick_patient'),
    path('register/', IAM.views.UserCreationForm2View.as_view(), name='register'),
    path('BestellungBestätigen/', views.medikamentenanfrageOffen, name='register'),
    path('apotheke_ueberblick/', views.ueberblick_apotheke, name="ueberblick_apotheke"),
    path('iCalLaden/<int:bestell_id>/', views.iCalErstellen, name="iCalErstellen"),
    path('getUserData/<int:patient_id>/', views.getUserData, name="getUserData"),
    path('', views.medikamentBestellen),
]
