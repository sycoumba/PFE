from django.shortcuts import render
from PRDV.models import Rdv
from patient.models import Patient
# Create your views here.


def login(request): 
    context = {} 
    return render(request, 'accueil/login.html', context)
     
 
""" def add(request):
 context = {}
 return render(request, 'patient/liste_patient.html', context) """
 #return render(request, 'accueil/home.html', context)

def liste(request):
      rendez_vous= Rdv.objects.all()
      patients=  Patient.objects.all()
      context = {'rendez_vous':rendez_vous, 'patients':patients}
      return render(request, 'patient/liste_patient.html', context)