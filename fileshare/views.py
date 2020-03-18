from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import date, datetime
import time
from threading import Timer
from .models import Folder, File
# Create your views here.

def index(request):
    user_folders = Folder.objects.filter(user=request.user)
    user_files = File.objects.filter(user=request.user)
    all_folders = user_folders.filter(linkedfolder__isnull=True)
    all_files = user_files.filter(folder__isnull=True)
    context = { 'all_folders':all_folders,'all_files':all_files }
    return render(request,'fileshare/index.html',context)

def detail(request,folder_id):
    folder = get_object_or_404(Folder,pk=folder_id)
    files = folder.file_set.all()
    folders = folder.folder_set.all()
    # Try folder_set.all() when model is 'folder' instead of 'Folder'
    context={'folder':folder,'folders':folders,'files':files,'folder_id':folder_id}
    return render(request,'fileshare/details.html',context)

class FolderCreate(LoginRequiredMixin, CreateView):
    model = Folder
    fields = ['name','author']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FolderCreate, self).form_valid(form)

# I have to add linkedfolder value by default
