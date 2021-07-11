from django.conf.urls import url
from . import views
from django.urls import path
import IAM.views

urlpatterns = [
    path('medikamentenbestellung/', views.medikamentBestellen, name='medikament bestellen'),
    path('medikamentenplan/', views.medikamentenplanEinsehen, name='medikamentenbestellung'),
    path('medikamentenplanDetails/', views.medikamentenplanDetailsEinsehen, name='medikamentenplanDetails'),
    path('medikamentenanfrageOffen/', views.medikamentenanfrageOffen, name='medikamentenanfrageOffen'),
    path('login/', IAM.views.logUserIn, name='login'),
    path('krankenkasseLogin/', IAM.views.logUserIn2, name='krankenkasseLogin'),
    path('arzt_ueberblick/', views.ueberblick_arzt, name='views.ueberblick_arzt'),
    path('patient_ueberblick/', views.ueberblick_patient, name='views.ueberblick_patient'),
    path('register/', IAM.views.UserCreationForm2View.as_view(), name='views.register'),
    path('', views.medikamentBestellen),
]
