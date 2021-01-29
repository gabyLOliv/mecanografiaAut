import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from pages import models as m


# UUIDUser
# - - - - - - - - - - - - - - - - - - -
class UUIDUser(AbstractUser):
	
	TIPO = (
		(0, 'PADRÃO'),
		(1, 'ADMIN')
	)

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user_permissions = models.ManyToManyField(Permission, blank=True, related_name='uuiduser_set', related_query_name='user')
	matricula = models.CharField(max_length=12, unique=True)
	tipo_user = models.IntegerField(choices=TIPO, default=0)

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = 'user'
		verbose_name_plural = 'users'
