from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm  

class SignUpView(CreateView):
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy("login")  
    template_name = "registration/signup.html"

def home(request):
    """
    Домашняя страница
    """
    return render(request, 'home.html')

def user_login(request):
    """
    Страница входа в личный кабинет
    """
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)  
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
            else:
                messages.error(request, "Неверное имя пользователя или пароль.")
        else:
            messages.error(request, "Заполните все поля корректно.")
    else:
        form = CustomAuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

