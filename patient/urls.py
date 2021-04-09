from django.urls import path   
from . import views
urlpatterns = [
    
    path('', views.ajout_patient),
    path('', views.get_patient),
]
