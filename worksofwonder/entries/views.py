from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'entries/base.html')

def readers(request):
    return render(request, 'readers.html')

def writers(request):
    return render(request, 'writers.html')

def login(request):
    return render(request, 'login.html')