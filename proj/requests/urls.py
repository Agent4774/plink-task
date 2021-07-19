from django.urls import path
from . import views


urlpatterns = [
	path('save-request/', views.save_request, name='save_request'),
	path('filtered-requests/', views.get_filtered_requests, name='filtered_requests'),
]