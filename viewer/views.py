from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Photo

# Create your views here.

def home(request):
    images = Photo.objects.all()
    return render(request, 'index.html', {'title': 'home' ,'images': images})

def simple_upload(request):
    # TODO: Make a form to catch values to insert on database
    if request.method == 'POST' and request.FILES['myfile']:
        my_file = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(my_file.name, my_file)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html', {'title': 'Upload'})


