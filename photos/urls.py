from django.urls import path
from . import views


urlpatterns = [
    path('upload/', views.UploadPhotoView.as_view(), name='upload_photo')
]