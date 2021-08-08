from .models import Note, Todo
from django.contrib import admin


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
	pass


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
	pass