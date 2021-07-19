from . import views
from django.urls import path


urlpatterns = [
	# Notes
	path('list-create-notes/', views.NoteListCreateAPIView.as_view(), name='list_create_note'),
	path('note/<int:pk>/', views.NoteRetrieveUpdateDestoyView.as_view(), name='get_update_delete_note'),
	# To-Do's
	path('list-create-todos/', views.TodoListCreateAPIView.as_view(), name='list_create_todo'),
	path('todo/<int:pk>/', views.TodoRetrieveUpdateDestoyView.as_view(), name='get_update_delete_todo'),
]