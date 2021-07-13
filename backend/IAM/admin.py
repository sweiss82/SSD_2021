from django.contrib import admin
#from django.customauth.models import MyUser
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from rest.models import Rolle
from django.contrib.auth.models import User



from .models import User
# Register your models here.

class UserCreationForm2(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Bestätigung', widget=forms.PasswordInput)

    CHOICES = [('1', 'Arzt'),
               ('2', 'Patient'),
               ('3', 'Apotheke')]
    benutzerrolle=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
   # benutzerrolle1 = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('benutzername',)

    def setBenutzerrolle(self, br):
        self.benutzerrolle1=br

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('benutzername', 'password', 'benutzerrolle')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm2
    list_display = ('benutzername', 'benutzerrolle')
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('benutzername', 'password', 'benutzerrolle1')}),
        #('Personal info', {'fields': ('benutzerrolle',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('benutzername', 'benutzerrolle1', 'password1', 'password2')}
        ),
    )
    search_fields = ('benutzername',)
    ordering = ('benutzername',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
