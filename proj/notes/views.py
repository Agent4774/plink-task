from .models import Note, Todo
from .permissions import IsOwnerOrReadOnly
from .serializers import NoteSerializer, TodoSerializer
from rest_framework.generics import (
	ListCreateAPIView,
	RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated


class NoteListCreateAPIView(ListCreateAPIView):
		serializer_class = NoteSerializer
		permission_classes = [IsAuthenticated]

		def get_queryset(self):
				return Note.objects.filter(author=self.request.user)

		def perform_create(self, serializer):
				serializer.save(author=self.request.user)


class NoteRetrieveUpdateDestoyView(RetrieveUpdateDestroyAPIView):
		queryset = Note.objects.all()
		serializer_class = NoteSerializer
		permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class TodoListCreateAPIView(ListCreateAPIView):
		serializer_class = TodoSerializer
		permission_classes = [IsAuthenticated]

		def get_queryset(self):
				return Todo.objects.filter(author=self.request.user)

		def perform_create(self, serializer):
				serializer.save(author=self.request.user)


class TodoRetrieveUpdateDestoyView(RetrieveUpdateDestroyAPIView):
		queryset = Todo.objects.all()
		serializer_class = TodoSerializer
		permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]