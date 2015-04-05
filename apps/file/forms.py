from django import forms
from models import File

class FileUploadForm(forms.Form):

    #title = forms.CharField(max_length=255)
    file = forms.FileField();

class FileDeleteForm(forms.Form):
    uuid = forms.CharField(max_length=150)
