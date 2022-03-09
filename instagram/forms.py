from django import forms
from .models import Image , editprofile

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'
        labels={'photo':''}


class Editform(forms.ModelForm):
     class Meta:
        model=editprofile
        fields= '__all__'
