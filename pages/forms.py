from django import forms

from .models import *


class NotificacaoForm(forms.ModelForm):

    class Meta:

        model = Notificacao
        fields = '__all__'