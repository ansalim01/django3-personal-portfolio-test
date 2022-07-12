import imp
from django.shortcuts import render
from .models import Proekt

# Create your views here.

def home(request):
    proekts=Proekt.objects.all()
    return render(request,'portfolio/home.html',{'proekts':proekts})
