from django.shortcuts import render,redirect 
from django.contrib import messages
from django.http import HttpResponse
from .models import Articles
from .forms import ArticleForm


# Create your views here.
def index(request):
    return render(request, 'entries/index.html')

def readers(request):
    context={
        'articles':Articles.objects.all()
    }
    return render(request, 'entries/readers.html',context)

def writers(request):
    return render(request, 'entries/writers.html')

def login(request):
    return render(request, 'login.html')

def upload(request):
    if request.method == 'POST':
        upload_form = ArticleForm(request.POST)
        if  upload_form.is_valid():
            upload_form.save()
            username =  upload_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} ')
            return redirect('readers')
    else:
            upload_form = ArticleForm()
    return render(request, 'entries/upload.html', {'upload_form': upload_form})

def about(request):
    return render(request, 'entries/about.html')

def contact(request):
    return render(request, 'entries/contact.html')