# FileEncoderProject/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('file-encoder/', include('FileEncoder.urls')),  # Include the urls from the FileEncoder app
    path('', include('FileEncoder.urls')),
]
