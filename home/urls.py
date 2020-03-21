from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.users,name='users'),
    path('<int:pk>', views.userindex,name='userindex'),
    path('detail/<int:folder_id>', views.userdetails,name='userdetails'),
    path('search/ff', views.searchff,name='search-ff'),
    path('search/users', views.searchusers,name='search-users'),
]