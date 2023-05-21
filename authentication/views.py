
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib import messages

from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import SignUpForm


class MyLogin(LoginView):
    template_name = 'authentication/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Vous êtes connecté avec succès.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'La connexion a échoué. Veuillez vérifier vos identifiants.')
        return super().form_invalid(form)
class MyLogout(LogoutView):
    next_page = reverse_lazy('authentication:login')
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Vous avez été déconnecté avec succès.")
        return super().dispatch(request, *args, **kwargs)

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'authentication/password_change.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Votre mot de passe a été modifié avec succés.')
        return super().form_valid(form)


class SignUpPage(View):
    form_class = SignUpForm
    template_name = "authentication/signup.html"
    success_url = settings.LOGIN_REDIRECT_URL

    def get(self, request, *args, **kwargs):
        return render(
            request,
            template_name=self.template_name,
            context={"form":self.form_class}
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        return render(
            request,
            template_name=self.template_name,
            context={"form":form}
        )