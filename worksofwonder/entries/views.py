from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'entries/index.html')

def readers(request):
    return render(request, 'entries/readers.html')

def writers(request):
    return render(request, 'entries/writers.html')

def login(request):
    return render(request, 'login.html')