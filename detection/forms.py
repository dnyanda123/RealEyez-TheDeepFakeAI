from django import forms
from .models import Image

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'title']
