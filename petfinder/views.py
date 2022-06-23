from django.shortcuts import render
from .models import Photos,Profile,Comment,Post

def home(request):
    photo = Photos.objects.all()
    ctx = {'photo':photo}
    return render(request,'index.html', ctx)


        