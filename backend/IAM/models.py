from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from rest.models import Rolle
#from applications.users.model import User

class MyUserManager(BaseUserManager):
    def create_user(self, benutzername, benutzerrolle, password=None):

        if not benutzername:
            raise ValueError("Benutzername fehlt!")
        if not benutzerrolle:
            raise ValueError("Rolle fehlt!")
        if not password:
            raise ValueError("Passwort fehlt!")

        user = self.model(benutzername=benutzername, benutzerrolle=benutzerrolle)
        user.setPasswort(password)
        user.save(self._db)
        return user

class User(AbstractBaseUser):
    benutzername = models.CharField(max_length=100, unique=True)
    benutzerrolle = models.ForeignKey(Rolle, on_delete=models.CASCADE, null=True)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELDS = 'benutzername'
    REQUIRED_FIELDS = ['benutzerrolle']


