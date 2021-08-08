from django.db import models


class Request(models.Model):
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=16)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	ip = models.GenericIPAddressField()

	def __str__(self):
		return f'By {self.email}'

	class Meta:
		verbose_name = 'Request'
		verbose_name_plural = 'Requests'