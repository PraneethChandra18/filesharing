from django.shortcuts import render,get_object_or_404
from .models import Folder, File
# Create your views here.

def index(request):
    all_folders = Folder.objects.all()
    context = { 'all_folders':all_folders, }
    return render(request,'fileshare/index.html',context)

def detail(request,folder_id):
    folder = get_object_or_404(Folder,pk=folder_id)
    files = folder.file_set.all()
    context={'folder':folder,'files':files}
    return render(request,'fileshare/details.html',context)
