from django import forms
from .models import IT_Posts
from django.contrib.auth import get_user_model

user=get_user_model()

class PostForm(forms.ModelForm):
    class Meta:
        model= IT_Posts
        fields=('name', 'description', 'pdf',)


class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.PasswordInput()
