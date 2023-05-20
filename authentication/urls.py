from django.contrib.auth.views import LoginView
from django.urls import path
from .views import logout_user

urlpatterns = [
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
         name='login'),
    path('logout/', logout_user, name='logout'),
]