from django.urls import path
from .views import home, SignUpView, user_login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),  
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', user_login, name='login'), 
    path('logout/', LogoutView.as_view(), name='logout'),
]
