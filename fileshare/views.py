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
from .forms import FolderForm, FileForm, FolderUploadForm
import requests
import os, io
import zipfile
from django.http import FileResponse, HttpResponse
from django.utils.text import slugify

# Create your views here.

def index(request):
    user_folders = Folder.objects.filter(user=request.user)
    user_files = File.objects.filter(user=request.user)
    all_folders = user_folders.filter(linkedfolder__isnull=True)
    all_files = user_files.filter(folder__isnull=True)
    context = { 'all_folders':all_folders,'all_files':all_files }
    return render(request,'fileshare/index.html',context)
#-----------------------------------------------------------------------------------------------------
def detail(request,folder_id):
    folder = get_object_or_404(Folder,pk=folder_id)
    files = folder.file_set.all()
    folders = folder.folder_set.all()
    # Try folder_set.all() when model is 'folder' instead of 'Folder'
    temp = folder
    parent_list = []
    parent_list.append(temp)
    while temp.linkedfolder:
        parent = temp.linkedfolder
        parent_list.append(parent)
        temp = parent
    active_folder = parent_list[0]
    parent_list.reverse()
    context={'folder':folder,'folders':folders,'files':files,'folder_id':folder_id,'parent_list':parent_list,'active_folder':active_folder}
    return render(request,'fileshare/details.html',context)
#------------------------------------------------------------------------------------------------------
class FolderCreate(LoginRequiredMixin, CreateView):
    model = Folder
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FolderCreate, self).form_valid(form)

# def Folder_Create(request,pk):
#     if request.method == 'POST':
#         form = FolderForm(request.POST)
#
#         if form.is_valid():
#             new_folder = form.save(commit=False)
#             new_folder.linkedfolder = Folder.objects.get(pk=pk)
#             new_folder.user = request.user
#             new_folder.save()
#             return redirect('fileshare:detail',pk)
#         else :
#             return render(request,'fileshare/folder_form.html',{'form':form})
#     else :
#         form = FolderForm(None)
#         return render(request,'fileshare/folder_form.html',{'form':form})


def Folder_Create(request,pk):
    form = FolderForm(None)

    n = request.GET.get('name')
    new_folder = form.save(commit=False)
    new_folder.name = n
    new_folder.linkedfolder = Folder.objects.get(pk=pk)
    new_folder.user = request.user
    new_folder.save()
    return redirect('fileshare:detail',pk)
# Use modals(bootstrap) in form.html
#-----------------------------------------------------------------------------------------------------

class FolderDelete(DeleteView):
    model = Folder

    def get_success_url(self):
        f = Folder.objects.get(pk = self.kwargs['pk'])
        folder = f.linkedfolder
        if not folder:
            return reverse_lazy('fileshare:index')
        else:
            return reverse_lazy('fileshare:detail',kwargs={'folder_id': folder.pk})

    def get(self, *args, **kwargs):
            return self.post(*args, **kwargs)
    # the above get function is used to delete the model without confirmation.
#-----------------------------------------------------------------------------------------------------
class FolderUpdate(UpdateView):
    model = Folder
    fields = ['name']

#-----------------------------------------------------------------------------------------------------
def FolderUploadIndex(request):
    if request.method == 'POST':
        form = FolderUploadForm(request.POST, request.FILES)
        p = request.POST['path']
        file_path_list = []
        t = ""
        for i in range(len(p)):
            if p[i]!=" ":
                t = t+p[i]
            else:
                file_path_list.append(t)
                t = ""

        pathlist_list = []

        for path in file_path_list:
            t = ""
            list = []
            for i in range(len(path)):
                if path[i]!='/':
                    t = t + path[i]
                else:
                    list.append(t)
                    t = ""
            pathlist_list.append(list)

        for path in pathlist_list:
            for i in range(len(path)):
                if i==0:
                    try:
                        fol = Folder.objects.get(linkedfolder__isnull=True,name=path[i])
                    except Folder.DoesNotExist:
                        new_folder = Folder(name=path[i],user=request.user)
                        new_folder.save()
                        path[i] = new_folder
                    else:
                        path[i] = fol
                else:
                    try:
                        fol = Folder.objects.get(linkedfolder=path[i-1],name=path[i])
                    except Folder.DoesNotExist:
                        new_folder = Folder(name=path[i],linkedfolder=path[i-1],user=request.user)
                        new_folder.save()
                        path[i] = new_folder
                    else:
                        path[i] = fol


        if form.is_valid():
            index = 0
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    pa = pathlist_list[index]
                    folder = pa[len(pa)-1]
                    f = File(file=formfile,user=request.user,folder=folder )
                    f.name = f.filename()
                    f.save()
                    index = index+1

        return redirect('fileshare:index')
    else:
        form = FolderUploadForm(None)
        return render(request,'fileshare/folder_upload.html',{'form':form})

def FolderUpload(request,pk):
    if request.method == 'POST':
        form = FolderUploadForm(request.POST, request.FILES)
        p = request.POST['path']
        file_path_list = []
        t = ""
        for i in range(len(p)):
            if p[i]!=" ":
                t = t+p[i]
            else:
                file_path_list.append(t)
                t = ""

        pathlist_list = []

        for path in file_path_list:
            t = ""
            list = []
            for i in range(len(path)):
                if path[i]!='/':
                    t = t + path[i]
                else:
                    list.append(t)
                    t = ""
            pathlist_list.append(list)

        for path in pathlist_list:
            for i in range(len(path)):
                if i==0:
                    try:
                        link = Folder.objects.get(pk=pk)
                        fol = Folder.objects.get(linkedfolder=link,name=path[i])
                    except Folder.DoesNotExist:
                        new_folder = Folder(name=path[i],linkedfolder=link,user=request.user)
                        new_folder.save()
                        path[i] = new_folder
                    else:
                        path[i] = fol
                else:
                    try:
                        fol = Folder.objects.get(linkedfolder=path[i-1],name=path[i])
                    except Folder.DoesNotExist:
                        new_folder = Folder(name=path[i],linkedfolder=path[i-1],user=request.user)
                        new_folder.save()
                        path[i] = new_folder
                    else:
                        path[i] = fol


        if form.is_valid():
            index = 0
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    pa = pathlist_list[index]
                    folder = pa[len(pa)-1]
                    f = File(file=formfile,user=request.user,folder=folder )
                    f.name = f.filename()
                    f.save()
                    index = index+1

        return redirect('fileshare:detail',pk)
    else:
        form = FolderUploadForm(None)
        return render(request,'fileshare/folder_upload.html',{'form':form})

#-----------------------------------------------------------------------------------------------------
# class FileAdd(CreateView):
#     model = File
#     fields = ['file']
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         obj = form.save(commit=False)
#         if self.request.FILES:
#             for f in self.request.FILES.getlist('file'):
#                 obj = File(file=f,user=self.request.user)
#
#         return super(FileAdd, self).form_valid(form)



        # form.instance.user = self.request.user
        # for field in self.request.FILES.keys():
        #     for f in self.request.FILES.getlist(field):
        #         fi = File(file=f,user=self.request.user)
        #         fi.save()
#----------------------------------------------------------------------------------------------------------

def AddFile(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    f = File(file=formfile,user=request.user)
                    f.name = f.filename()
                    f.save()
            return redirect('fileshare:index')
        else:
            return render(request,'fileshare/file_form.html',{'form':form })
    else:
        form = FileForm(None)
        return render(request,'fileshare/file_form.html',{'form':form })

def AddLinkedFile(request,pk):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            for field in request.FILES.keys():
                for formfile in request.FILES.getlist(field):
                    f = File(file=formfile,user=request.user,folder=Folder.objects.get(pk=pk))
                    f.name = f.filename()
                    f.save()
            return redirect('fileshare:detail',pk)
        else:
            return render(request,'fileshare/file_form.html',{'form':form })
    else:
        form = FileForm(None)
        return render(request,'fileshare/file_form.html',{'form':form })
#--------------------------------------------------------------------------------------------------------

class FileDelete(DeleteView):
    model = File

    def get_success_url(self):
        f = File.objects.get(pk = self.kwargs['pk'])
        folder = f.folder
        if not folder:
            return reverse_lazy('fileshare:index')
        else:
            return reverse_lazy('fileshare:detail',kwargs={'folder_id': folder.pk})

    def get(self, *args, **kwargs):
            return self.post(*args, **kwargs)
#---------------------------------------------------------------------------------------------------------
class FileUpdate(UpdateView):
    model = File
    fields = ['name']

#---------------------------------------------------------------------------------------------------------

# def AddFolder(request):
#     if request.method == 'POST':
#         form = FolderUploadForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             for field in request.FILES.keys():
#                 for formfile in request.FILES.getlist(field):
#                     f = File(file=formfile,user=request.user)
#                     f.save()
#             return redirect('fileshare:index')
#         else:
#             return render(request,'fileshare/file_form.html',{'form':form })
#     else:
#         form = FolderUploadForm(None)
#         return render(request,'fileshare/file_form.html',{'form':form })
#
# def AddLinkedFolder(request,pk):
#     if request.method == 'POST':
#         form = FolderUploadForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             for field in request.FILES.keys():
#                 for formfile in request.FILES.getlist(field):
#                     f = File(file=formfile,user=request.user,folder=Folder.objects.get(pk=pk))
#                     f.save()
#             return redirect('fileshare:detail',pk)
#         else:
#             return render(request,'fileshare/file_form.html',{'form':form })
#     else:
#         form = FolderUploadForm(None)
#         return render(request,'fileshare/file_form.html',{'form':form })
#----------------------------------------------------------------------------------------------------------

def select(request,pk):
    folder = get_object_or_404(Folder,pk=pk)
    files = folder.file_set.all()
    folders = folder.folder_set.all()
    context={'folder':folder,'folders':folders,'files':files}
    return render(request,'fileshare/select.html',context)

def list_delete(request,pk):
    folder_list = request.GET.getlist('folder')
    file_list = request.GET.getlist('file')
    for p in folder_list:
        folder = Folder.objects.get(pk=p)
        folder.delete()
    for p in file_list:
        file = File.objects.get(pk=p)
        file.delete()
    return redirect('fileshare:detail',pk)

def download_file(request,pk):
    item = get_object_or_404(File, pk=pk)
    file_name, file_extension = os.path.splitext(item.file.file.name)
    file_extension = file_extension[1:] # removes dot
    x = -1*len(file_extension)
    response = FileResponse(item.file.file,
        content_type = "file/%s" % file_extension)
    response["Content-Disposition"] = "attachment;"\
        "filename=%s.%s" %(slugify(item.name)[:x], file_extension)
    return response

def list_download(request):
    file_list = request.GET.getlist('file')
    zip_subdir = "download_folder"
    zip_filename = zip_subdir + ".zip"
    byte_stream = io.BytesIO()
    zf = zipfile.ZipFile(byte_stream, "w")

    zf = filelistdownload(file_list,zf,zip_subdir)
    zf.close()
    response = HttpResponse(byte_stream.getvalue(), content_type="application/x-zip-compressed")
    response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    return response

#This function is used to use list_download recursive
def filelistdownload(file_list,zf,zip_subdir):
    for p in file_list:
        item = get_object_or_404(File, pk=p)
        file_name, file_extension = os.path.splitext(item.file.file.name)
        file_extension = file_extension[1:] # removes dot
        x = -1*len(file_extension)
        response = HttpResponse(item.file.file,
            content_type = "file/%s" % file_extension)
        response["Content-Disposition"] = "attachment;"\
            "filename=%s.%s" %(slugify(item.file.name)[:x], file_extension)

        filename = slugify(item.name)[:x]
        filename = filename + "." + file_extension
        f1 = open(filename , 'wb')
        f1.write(response.content)
        f1.close()

        zip_path = os.path.join(zip_subdir, filename)
        zf.write(filename, zip_path)

    # This loop is to remove those files which are being created due to f1.write()
    for p in file_list:
        item = get_object_or_404(File, pk=p)
        file_name, file_extension = os.path.splitext(item.file.file.name)
        file_extension = file_extension[1:] # removes dot
        x = -1*len(file_extension)
        filename = slugify(item.name)[:x]
        filename = filename + "." + file_extension

        location = os.path.abspath(filename)
        os.remove(location)

    return zf


def download_folder(request,pk):
    folder = get_object_or_404(Folder, pk=pk)
    folder_name = folder.name
    zip_subdir = folder_name
    zip_filename = zip_subdir + ".zip"
    byte_stream = io.BytesIO()
    zf = zipfile.ZipFile(byte_stream, "w")

    folder_list = Folder.objects.filter(linkedfolder=folder)
    file_list = File.objects.filter(folder=folder)

    zf = zip_them_all(file_list,folder_list,zip_subdir,zf)

    zf.close()
    response = HttpResponse(byte_stream.getvalue(), content_type="application/x-zip-compressed")
    response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    return response

#This function is used to use download_folder recursive
def zip_them_all(file_list,folder_list,zip_path,zf):
    for p in file_list:
        item = p
        file_name, file_extension = os.path.splitext(item.file.file.name)
        file_extension = file_extension[1:] # removes dot
        x = -1*len(file_extension)
        response = HttpResponse(item.file.file,
            content_type = "file/%s" % file_extension)
        response["Content-Disposition"] = "attachment;"\
            "filename=%s.%s" %(slugify(item.name)[:x], file_extension)

        filename = slugify(item.name)[:x]
        filename = filename + "." + file_extension
        f1 = open(filename , 'wb')
        f1.write(response.content)
        f1.close()

        pa = os.path.join(zip_path,filename)
        zf.write(filename,pa, zipfile.ZIP_DEFLATED)

    # This loop is to remove those files which are being created due to f1.write()
    for p in file_list:
        item = p
        file_name, file_extension = os.path.splitext(item.file.file.name)
        file_extension = file_extension[1:] # removes dot
        x = -1*len(file_extension)
        filename = slugify(item.name)[:x]
        filename = filename + "." + file_extension

        location = os.path.abspath(filename)
        os.remove(location)


    for p in folder_list:
        dir = p.name
        z_path = os.path.join(zip_path, dir)
        fo_list = Folder.objects.filter(linkedfolder=p)
        fi_list = File.objects.filter(folder=p)
        zf = zip_them_all(fi_list,fo_list,z_path,zf)


    return zf

def list_folder_file_download(request):
    file_list = request.GET.getlist('file')
    folder_list = request.GET.getlist('folder')

    zip_subdir = "download_folder"
    zip_filename = zip_subdir + ".zip"
    byte_stream = io.BytesIO()
    zf = zipfile.ZipFile(byte_stream, "w")

    fi_list = File.objects.none()
    fo_list = Folder.objects.none()

    for f in file_list:
        fi_list = fi_list | File.objects.filter(pk=f)

    for f in folder_list:
        fo_list = fo_list | Folder.objects.filter(pk=f)

    zf = zip_them_all(fi_list,fo_list,zip_subdir,zf)

    zf.close()
    response = HttpResponse(byte_stream.getvalue(), content_type="application/x-zip-compressed")
    response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    return response


def selectindex(request):
    user_folders = Folder.objects.filter(user=request.user)
    user_files = File.objects.filter(user=request.user)
    all_folders = user_folders.filter(linkedfolder__isnull=True)
    all_files = user_files.filter(folder__isnull=True)
    context = { 'folders':all_folders,'files':all_files }
    return render(request,'fileshare/selectindex.html',context)


def list_delete_index(request):
    folder_list = request.GET.getlist('folder')
    file_list = request.GET.getlist('file')
    for p in folder_list:
        folder = Folder.objects.get(pk=p)
        folder.delete()
    for p in file_list:
        file = File.objects.get(pk=p)
        file.delete()
    return redirect('fileshare:index')





# Todo

#  Folder Upload
