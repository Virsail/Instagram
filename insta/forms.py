from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm
from django.contrib .auth.models import User
from pyuploadcare.dj.forms import ImageField



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class StoryForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude =['posted_by','profile','likes']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude =['poster','image']
