from django.db import models
    
from django import forms
#from models import Patient
# Create your models here.

class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=150)
    age = models.TextField(null=True)
    sexe = models.TextField(null=True)
    adresse = models.TextField(null=False)
     
    def __str__(self):
     return self.nom
    

