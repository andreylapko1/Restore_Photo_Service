from django import forms

from photos.models import Photos


class UploadPhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['original_photo']