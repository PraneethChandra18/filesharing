from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import os
# Create your models here.


class Folder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=50)
    linkedfolder = models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True)
    lastmodified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('fileshare:index')

    def __str__(self):
        return self.name 

class File(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    folder=models.ForeignKey(Folder,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    file=models.FileField(upload_to='files');
    created_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        f = File.objects.get(pk = self.pk)
        folder = f.folder
        if not folder:
            return reverse('fileshare:index')
        else:
            return reverse('fileshare:detail',kwargs={'folder_id': folder.pk})

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     self.name = self.filename()
    #     super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

# class FolderUpload(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
#     linkedfolder = models.ForeignKey(Folder,on_delete=models.CASCADE,null=True,blank=True)
#     folder = models.FileField();
#     created_on = models.DateTimeField(auto_now_add=True)
