from django import forms
from viewer.models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('nickname', 'pet_name', 'img_dir', 'rank')