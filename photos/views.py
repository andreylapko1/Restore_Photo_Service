from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView

from photos.forms import UploadPhotoForm


class UploadPhotoView(View):
    def get(self, request):
        form = UploadPhotoForm()
        return render(request, 'photos/upload.html', {'form':form})

    def post(self, request):
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # photo_file = form.cleaned_data['photo_file']
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()
            return render(request, 'photos/photo_waiting.html')
        return render(request, 'photos/upload.html', {'form': form})


def bootstrap_check(request):
    if request.method == 'GET':
        return render(request, 'photos/bootstrap.html')


