from django.db import models
from core import models as m

class Formulario(models.Model):
    
	TIPO = (
        (0, 'Frente'),
        (1, 'Frente e Verso'),
    )

	nome = models.CharField(max_length=50)
	disciplina = models.CharField(max_length=50)
	numero_de_copias = models.IntegerField()
	numero_de_paginas = models.IntegerField()
	tipo = models.IntegerField(choices=TIPO)
	user = models.ForeignKey(m.UUIDUser, on_delete=models.CASCADE, null=True, blank=True)

	def get_tipo(self):
		if self.tipo == 0:
			return 'Frente'
		elif self.tipo == 1:
			return'Frente e Verso'


class Notificacao(models.Model):

	TIPO = (
		(0, 'Aceito'),
		(1, 'Negado')
	)

	tipo = models.IntegerField(choices=TIPO)
	user = models.ForeignKey(m.UUIDUser, on_delete=models.CASCADE, null=True, blank=True)

	def aviso(self):
		if self.tipo == 0:
			return 'Seu pedido de impressão foi aceito'
		elif self.tipo == 1:
			return 'Seu pedido de impressão não atendia aos requisitos e por isso foi negado'
