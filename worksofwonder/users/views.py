from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import UserSignUpForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created {username}! ')
            return redirect('login')
    else:
        form = UserSignUpForm()
    return render(request, 'users/signup.html', {'form': form})


# def login(request):
#     form = AuthenticationForm()
#     return render(request = request,
#                   template_name = "users/login.html",
#                   context={"form":form})
