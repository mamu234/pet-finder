from django.contrib import admin
from django.urls import path
from .import views 
from django.contrib.auth import views as auth_views


urlpatterns = [
path('', views.home, name='home'),
path('upload/',views.upload,name='upload'),
path('update/<int:post_id>',views.update,name='update'),
path('delete/<int:post_id>',views.delete,name='delete'),
path('register/',views.register, name="register"),
path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
]

 



