from django import forms
from models import File

class FileForm(forms.Form):

    #title = forms.CharField(max_length=255)
    file = forms.FileField();
