from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('requests/', include('requests.urls')),
    path('api/requests/', include('requests.api.urls')),
    path('api/users/', include('users.urls')),
    path('api/notes/', include('notes.urls')),
]
