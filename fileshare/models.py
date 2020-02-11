from django.db import models

# Create your models here.


class Folder(models.Model):
    name = models.CharField(max_length=50)
    linkedfolder = models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True)
    author = models.CharField(max_length=100)
    lastmodified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class File(models.Model):
    folder=models.ForeignKey(Folder,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=50)
    file=models.CharField(max_length=250);
    info=models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
