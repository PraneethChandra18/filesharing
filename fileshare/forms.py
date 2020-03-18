from .models import Folder, File
from django import forms


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']
