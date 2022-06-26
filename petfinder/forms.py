from .models import Post
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UploadpostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields='__all__'