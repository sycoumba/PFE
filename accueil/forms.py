from django.forms import fields
from accueil import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class CreerUtilisateur(UserCreationForm):
    class Meta:
        models = User
        fields = ['username', 'email', 'password1', 'password2']
            
    