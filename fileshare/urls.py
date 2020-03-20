from django.urls import path, include
from . import views

app_name = 'fileshare'

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:folder_id>/',views.detail,name='detail'),
    path('folder/add/',views.FolderCreate.as_view(),name='folder-add'),
    path('folder/add/<int:pk>',views.Folder_Create,name='linked-folder-add'),
    path('folder/delete/<int:pk>',views.FolderDelete.as_view(),name='folder-delete'),
    path('folder/update/<int:pk>',views.FolderUpdate.as_view(),name='folder-update'),
    path('file/add/',views.AddFile,name='file-add'),
    path('file/add/<int:pk>',views.AddLinkedFile,name='linked-file-add'),
    path('file/delete/<int:pk>',views.FileDelete.as_view(),name='file-delete'),
    path('file/update/<int:pk>',views.FileUpdate.as_view(),name='file-update'),
    # path('folder/upload/',views.AddFolder,name='folder-upload'),
    # path('folder/upload/<int:pk>',views.AddLinkedFolder,name='linked-folder-upload'),
]
