from django.urls import path, include
from . import views

app_name = 'fileshare'

urlpatterns = [
    path('', views.index,name='index'),
    path('<int:pk>',views.detail,name='detail'),
    path('add/<int:pk>',views.folder_create,name='folder-add'),

]
