from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from datetime import date, datetime
import time
from threading import Timer
from .models import Folder, File
from .forms import FolderForm
# Create your views here.

def index(request):
    user_folders = Folder.objects.filter(user=request.user)
    user_files = File.objects.filter(user=request.user)
    all_folders = user_folders.filter(linkedfolder__isnull=True)
    all_files = user_files.filter(folder__isnull=True)
    context = { 'all_folders':all_folders,'all_files':all_files }
    return render(request,'fileshare/index.html',context)

def detail(request,pk):
    folder = get_object_or_404(Folder,pk=pk)
    files = folder.file_set.all()
    folders = folder.folder_set.all()
    # Try folder_set.all() when model is 'folder' instead of 'Folder'
    context={'folder':folder,'folders':folders,'files':files,'pk':pk}
    return render(request,'fileshare/details.html',context)
@login_required
def folder_create(request, pk):
    folder = get_object_or_404(Folder,pk= pk)
    if request.method =="POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            new_folder=form.save(commit=False)
            new_folder.linkedfolder=folder
            new_folder.user=request.user
            new_folder.save() 
            return redirect('fileshare:detail', folder.pk)
    else:
        form = FolderForm()
    return render(request, 'fileshare/folder_form.html', {'form': form})

    
    
#  model = Folder
 #   fields = ['name','author']
  #def form_valid(self, form):
    #    form.instance.user = self.request.user
     #   return super(FolderCreate, self).form_valid(form)"""

# I have to add linkedfolder value by default
