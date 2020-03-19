from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
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
    name = models.CharField(max_length=50)
    file=models.FileField()
    info=models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
