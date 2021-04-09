from patient.models import Patient
from django.db.models.query import QuerySet
from django.http import request
from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from .forms import ContactForm

# Create your views here.
def ajout_patient(request):  
 context = {}
 return render(request, 'patient/add_patient.html', context)

def get_patient(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
                # create a form instance and populate it with data from the request:
            form = ContactForm(request.POST, QuerySet = Patient.objects.all())
                # check whether it's valid:
            if form.is_valid():
                form.save()
                    # process the data in form.cleaned_data as required
          
                    # redirect to a new URL:
                return HttpResponseRedirect(request, '/patient/liste_patient.html')
                # if a GET (or any other method) we'll create a blank form
    else:
            form = ContactForm()
            context ={'form':form}
            return render(request, 'erreur_404.html', context) 