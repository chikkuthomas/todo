from  django import forms
from django.forms import ModelForm
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TodoForm(ModelForm):
    class Meta:
        model=Todo
        fields=["task_name"]
        widgets={

            "task_name":forms.TextInput(attrs={"class":"form-control"}),

        }

class TodoSearchForm(forms.Form):
    created_by=forms.CharField(max_length=120,widget=forms.TextInput(attrs={"class":"form-control"}))

class RegisterationForm(UserCreationForm):
    password1 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["first_name","username","email","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"})
        }
class LoginForm(forms.Form):
    username=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}))



