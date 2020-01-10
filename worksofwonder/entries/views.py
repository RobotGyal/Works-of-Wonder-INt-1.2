from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles


# Create your views here.
def index(request):
    return render(request, 'entries/index.html')

def readers(request):
    context={
        'items':Articles.objects.all()
    }
    return render(request, 'entries/readers.html',context)

def writers(request):
    return render(request, 'entries/writers.html')

def login(request):
    return render(request, 'login.html')