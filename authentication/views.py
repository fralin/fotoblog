
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages


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