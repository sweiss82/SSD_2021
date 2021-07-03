from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .serializer import *

class MedikamentenbestellungSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medikamentenbestellung
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
