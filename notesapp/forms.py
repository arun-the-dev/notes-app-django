from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Notes,Profile


class NotesCreateForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ["title","content"]
class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","email"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_pic"]