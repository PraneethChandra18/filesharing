from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import date, datetime
import time
from threading import Timer
import os
from fileshare.models import Folder, File
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.

def users(request):
    all_users = User.objects.all()
    current_user = request.user
    return render(request,'home/users.html',{'all_users': all_users,'current_user':current_user})

def userindex(request,pk):
    user = User.objects.get(pk=pk)
    user_folders = Folder.objects.filter(user=user)
    user_files = File.objects.filter(user=user)
    all_folders = user_folders.filter(linkedfolder__isnull=True)
    all_files = user_files.filter(folder__isnull=True)
    context = { 'all_folders':all_folders,'all_files':all_files }

    return render(request,'home/userindex.html',context)

def userdetails(request,folder_id):
    folder = get_object_or_404(Folder,pk=folder_id)
    files = folder.file_set.all()
    folders = folder.folder_set.all()
    # Try folder_set.all() when model is 'folder' instead of 'Folder'
    context={'folder':folder,'folders':folders,'files':files,'folder_id':folder_id}
    return render(request,'home/userdetails.html',context)

def searchff(request):
    all_users = User.objects.all()
    query = request.GET.get('q')
    if query:
        all_folders = Folder.objects.filter(Q(name__icontains=query))
        all_files = File.objects.filter(Q(name__icontains=query))
        context = { 'all_folders':all_folders,'all_files':all_files }
        return render(request,'home/userindex.html',context)

    else:
        return render(request,'home/users.html',{'all_users': all_users})

def searchusers(request):
    all_users = User.objects.all()
    current_user = request.user

    query = request.GET.get('q')
    if query:
        users = User.objects.filter(Q(username__icontains=query))
        context = { 'all_users':users,'current_user':current_user }
        return render(request,'home/users.html',context)

    else:
        return render(request,'home/users.html',{'all_users': all_users,'current_user':current_user})
