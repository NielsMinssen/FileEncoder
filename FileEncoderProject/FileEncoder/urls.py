# FileEncoder/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.file_upload_view, name='file-upload'),  # URL for file uploading
    path('', views.file_upload_view, name='home')
]
