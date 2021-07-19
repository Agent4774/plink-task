from .models import Note, Todo
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
		class Meta:
				model = Note
				fields = ('text', 'created')


class TodoSerializer(serializers.ModelSerializer):
		class Meta:
				model = Todo
				fields = ('text', 'created')