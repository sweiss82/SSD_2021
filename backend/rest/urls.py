from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('medikamentenbestellung/', views.medikamentBestellen, name='medikament bestellen'),
    path('medikamentenplan/', views.medikamentenplanEinsehen, name='medikamentenbestellung'),
    path('medikamentenplanDetails/', views.medikamentenplanDetailsEinsehen, name='medikamentenplanDetails'),
    path('medikamentenanfrageOffen/', views.medikamentenanfrageOffen, name='medikamentenanfrageOffen'),
    path('login/', views.Einloggen, name='login'),
    path('krankenkasseLogin/', views.krankenkasseLogin, name='krankenkasseLogin'),
    path('arzt_ueberblick/', views.ueberblick_arzt, name='views.ueberblick_arzt'),
    path('patient_ueberblick/', views.ueberblick_patient, name='views.ueberblick_patient'),
    path('', views.medikamentBestellen),
]
