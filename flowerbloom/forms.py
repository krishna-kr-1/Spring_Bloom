
#flowerbloom/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . models import MyUser

class MyRegFrm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("username", "first_name", "last_name", "email")

class LoginFrm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ("email")
