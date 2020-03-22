from .models import Folder, File #FolderUpload
from django import forms


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

class FileForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = File
        fields = ['file']

# class FolderUploadForm(forms.ModelForm):
#     folder = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'webkitdirectory': True, 'directory': True}))
#
#     class Meta:
#         model = FolderUpload
#         fields = ['folder']
