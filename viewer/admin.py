from django.contrib import admin
from .models import Photo

class AdminPhoto(admin.ModelAdmin):
    list_display = ['nickname', 'petname', 'image url', 'rank']

    class Meta:
        model = Photo

# Register your models here.
admin.site.register(Photo)