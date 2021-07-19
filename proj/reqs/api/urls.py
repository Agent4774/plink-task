from . import views
from django.urls import path


urlpatterns = [
	path('save-request/', views.RequestCreateAPIView.as_view(), name='api_save_request'),
	path('filtered-requests/', views.FilteredRequestsAPIView.as_view(), name='api_filtered_requests'),
]