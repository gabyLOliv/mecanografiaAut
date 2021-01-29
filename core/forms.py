from django import forms
from django.contrib.auth import authenticate

from .models import UUIDUser


# User: create
class UUIDUserForm(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    def save(self, commit=True):
        user = super(UUIDUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = UUIDUser
        form = forms.ModelForm
        fields = ('username', 'matricula', 'password')
        labels = {
            'username': 'Nome',
            'matricula': 'Matricula',
            'password': 'Senha',
        }


# UUIDUser: login
class UUIDUserLoginForm(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = UUIDUser
        fields = ('matricula', 'password')
        labels = {
            'matricula': 'Matricula',
            'password': 'Senha',
        }
