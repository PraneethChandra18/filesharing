from django.shortcuts import render,get_object_or_404
from .models import Folder, File
# Create your views here.

def index(request):
    all_folders = Folder.objects.filter(linkedfolder__isnull=True)
    all_files = File.objects.filter(folder__isnull=True)
    context = { 'all_folders':all_folders,'all_files':all_files }
    return render(request,'fileshare/index.html',context)

def detail(request,folder_id):
    folder = get_object_or_404(Folder,pk=folder_id)
    files = folder.file_set.all()
    folders = folder.folder_set.all()
    context={'folder':folder,'folders':folders,'files':files,'folder_id':folder_id}
    return render(request,'fileshare/details.html',context)
