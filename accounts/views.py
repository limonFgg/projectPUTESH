from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render

class SignUpView(CreateView):
    form_class = UserCreationForm
    # success_url = reverse_lazy("login")
    templates_name = "registration/signup.html"


def home(request):
    
    'Домашняя страница'
    
    return render(request, 'home.html')

def user_signup(request):
    '''
    страница регистрации
    '''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})



def user_login(request):
    '''
    страница входа в личный кабинет
    '''
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            username = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        else:
            form = Loginform()
        return render(request, 'login.html', {'form': form})