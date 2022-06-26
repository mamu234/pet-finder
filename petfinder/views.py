from django.http import HttpResponse
from django.shortcuts import render,redirect
from requests import request
from .models import Photos,Profile,Comment,Post,User
from django.contrib import messages
from .forms import *
from django.views.generic import DetailView,TemplateView
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserCreationForm


# Create your views here.


def home(request):
    return render(request,"index.html")

def register(request):
    '''
    Function to register new users to the database.
    '''
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"You have succesfully created an account. Proceed to Login")
            return redirect('login')



    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request,"sign-up.html",context)
  
       
def upload(request):
    upload=UploadpostForm()
    if request.method=='POST':
        upload=UploadpostForm(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('home')
        else:
            return HttpResponse('Your form is wrong')
    else:
        return render(request,'upload.html',{'upload':upload})

def update(request,post_id):
    post_id=int(post_id)
    try:
     blog_up=Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return redirect('home')
    post_form=UserCreationForm(request.POST or None,instance=blog_up)
    if post_form.is_valid():
        post_form.save()
        return redirect('home')
    return render (request,'upload_form.html',{'upload':post_form})

def delete(request,blog_id):
    post_id=int(post_id)
    try:
        blog_up=Post.objects.get(id=blog_id)
    except Post.DoesNotExist:
        return redirect('index.html')
    blog_up.delete()
    return redirect('index.html')

def register(request):
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request,"register.html",context)

