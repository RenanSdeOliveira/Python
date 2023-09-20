from django.contrib import admin
from django.urls import path, include
from register.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_register/', register),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('rest_api.urls', namespace='api'))
]