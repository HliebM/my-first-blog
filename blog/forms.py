from django import forms
from .models import Post
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('comment',)