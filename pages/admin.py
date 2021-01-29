from django.contrib import admin
from . import models


class Formulario(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.Formulario)
admin.site.register(models.Notificacao)
