from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('medikamentenbestellung/', views.medikamentBestellen, name='medikament bestellen'),
    path('medikamentenplan/', views.medikamentenplanEinsehen, name='medikamentenbestellung'),
    path('medikamentenplanDetails/', views.medikamentenplanDetailsEinsehen, name='medikamentenplanDetails'),
    path('medikamentenanfrageOffen/', views.medikamentenanfrageOffen, name='medikamentenanfrageOffen'),
    path('', views.medikamentBestellen),
]
