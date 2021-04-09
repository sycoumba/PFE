from patient.models import Patient
from django.db import models
from django.utils import timezone
from patient.models import Patient

# Create your models here.


class Rdv(models.Model):
    date_rdv = models.DateTimeField(default=timezone.now, blank=True, null=False)
    status = models.CharField(max_length=150, blank=True, null=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
   
   
   