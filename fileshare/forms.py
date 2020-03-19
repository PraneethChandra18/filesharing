from django import forms

from .models import Folder,File

 
class FolderForm(forms.ModelForm):
    class Meta:
        model= Folder
        fields = ('author', 'name',)