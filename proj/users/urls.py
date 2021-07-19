from . import views
from django.urls import path


urlpatterns = [
	path('register/', views.UserCreateAPIView.as_view(), name='register'),
	path('login/', views.UserLoginAPIView.as_view(), name='login'),
]