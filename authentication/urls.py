from django.contrib.auth.views import LoginView
from django.urls import path
from .views import MyLogin, MyLogout, MyPasswordChangeView, SignUpPage

app_name = 'authentication'

urlpatterns = [
    path('', MyLogin.as_view(), name='login'),
    path('password-change/',MyPasswordChangeView.as_view(), name='password-change/'),
    path('logout/', MyLogout.as_view(), name='logout'),
    path('signup/', SignUpPage.as_view(), name='signup'),
]