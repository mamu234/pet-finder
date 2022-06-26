# from distutils.command.upload import upload
# from django.db import models
# from django.forms import CharField, IntegerField
# from .models import *
# from cloudinary.models import CloudinaryField
# from django.contrib.auth.models import User


# # Create your models here.
# class Profile(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#   image= models.ImageField(upload_to='image',blank=True)
#   location = models.CharField(max_length=150,null=True)
#   bio=models.TextField(max_length=240)

#   def __str__(self):
#     return self.user


# class Post(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   dog_name =models.CharField(max_length=150, null=True)
#   image = models.ImageField(max_length=500, blank=True)
#   description=models.TextField(max_length=300)
#   color = models.CharField(max_length=150, blank=True)
#   gender = models.CharField(max_length=150, blank=True)
#   age = models.IntegerField(blank=True)
#   breed = models.CharField(max_length=200, blank=True)
#   size = models.IntegerField(blank=True)
#   created_at = models.DateTimeField(auto_now_add=True)

#   def __str__(self):
#     return self.dog_name

#   class Meta: 
#     ordering = ['-created_at']


# class Comment(models.Model):
#   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
#   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
#   content=models.CharField(max_length=1000)
#   created_at= models.DateTimeField(auto_now_add=True)

#   def __str__(self):
#     return self.user

#   class Meta: 
#     ordering = ['-created_at']

# class Photos(models.Model):
#     title = models.CharField(max_length=100)
#     image = CloudinaryField('image')
    
#     def __str__(self):
#         return self.title

from django.db import models

from cloudinary.models import CloudinaryField
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField, IntegerField, TextField, BooleanField, CharField
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Profile(Model):
  user = models.OneToOneField(User, on_delete=CASCADE, related_name='profile')
  avatar = CharField(max_length=500, blank=True)
  bio = TextField(max_length=2500, blank=True)
  location = CharField(max_length=150)
  org_name = CharField(max_length=150, blank=True)
  verified = BooleanField(default=False)

  def __str__(self):
    return self.user.username


class Post(Model):
  user = models.ForeignKey(User, on_delete=CASCADE, related_name='post')
  dog_name = models.CharField(max_length=150, blank=False)
  image = models.ImageField(max_length=500, blank=False)
  description = TextField(max_length=1500, blank=False)
  color = CharField(max_length=150, blank=True)
  gender = CharField(max_length=150, blank=True)
  friendly = CharField(max_length=200, blank=True)
  kids = CharField(max_length=200, blank=True)
  age = IntegerField(blank=True)
  breed = CharField(max_length=200, blank=True)
  size = IntegerField(blank=True)
  health = CharField(max_length=200, blank=True)
  active = CharField(max_length=200, blank=True)
  house_trained = BooleanField(default=False, blank=True)
  available = BooleanField(default=False, blank=False)
  created_at = DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.dog_name

  class Meta: 
    ordering = ['-created_at']


class Photos(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    
    
    def __str__(self):
        return self.title


class Comment(Model):
  user = models.ForeignKey(User, on_delete=CASCADE, related_name='comment')
  post = models.ForeignKey(Post, on_delete=CASCADE, related_name='comment')
  content = TextField(max_length=1000)
  created_at = DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  class Meta: 
    ordering = ['-created_at']

class Item(models.Model):
    name = models.CharField(max_length=200)
    Created = models.DateTimeField(auto_now_add=True)