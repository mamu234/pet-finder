from distutils.command.upload import upload
from django.db import models
from django.forms import BooleanField, CharField, IntegerField
from .models import Profile, Post,Comment
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  image= models.TextField(upload_to='image',blank=True)
  location = CharField(max_length=150)
  bio=models.TextField(max_length=240)

  def __str__(self):
    return self.user


class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
  dog_name =CharField(max_length=150, blank=False)
  image = models.CharField(max_length=500, blank=False)
  bio=models.TextField(max_length=300)
  color = models.CharField(max_length=150, blank=True)
  gender = models.CharField(max_length=150, blank=True)
  age = models.IntegerField(blank=True)
  breed = models.CharField(max_length=200, blank=True)
  size = models.IntegerField(blank=True)
  available = BooleanField(default=False, blank=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.dog_name

  class Meta: 
    ordering = ['-created_at']


class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
  content=models.CharField(max_length=1000)
  created_at= models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user

  class Meta: 
    ordering = ['-created_at']