from patient.models import Patient
from django.shortcuts import render
from PRDV import models
from django import forms
from django.db.models import fields


class ContactForm(forms.Form):
    class Meta:
        models = Patient
        fields = ['nom', 'prenom', 'telephone', 'age', 'sexe', 'adresse']
       