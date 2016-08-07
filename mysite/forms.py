from django import forms
from .models import Post, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('product','description','price',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=('schoolid','phone_number')
    

