from django.urls import path, include
from . import views

app_name = 'fileshare'

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:folder_id>',views.detail,name='detail'),
    path('folder/add',views.FolderCreate.as_view(),name='folder-add'),

]
