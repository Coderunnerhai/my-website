from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.conf import settings
import os

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle the uploaded file
            handle_uploaded_file(request.FILES['file'])
            return redirect('upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'uploader/upload.html', {'form': form})

def handle_uploaded_file(f):
    upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    with open(os.path.join(upload_dir, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_success(request):
    return render(request, 'uploader/upload_success.html')
