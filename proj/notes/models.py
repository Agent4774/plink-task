from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


User = get_user_model()


class Note(models.Model):
		text = models.TextField()
		author = models.ForeignKey(User, on_delete=models.CASCADE)
		created = models.DateTimeField(default=timezone.now)

		def __str__(self):
				return self.author.username


class Todo(models.Model):
		text = models.TextField()
		author = models.ForeignKey(User, on_delete=models.CASCADE)
		created = models.DateTimeField(default=timezone.now)

		def __str__(self):
				return self.author.username