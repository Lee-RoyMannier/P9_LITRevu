from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from authentication.forms import LoginForm, InscriptionForm
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView


# Create your views here.
class LoginHomePageView(LoginView):
    template_name = "authentication/home_page.html"
    form_class = LoginForm
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'You have successfully logged in.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Nom d'utilisateur ou mot de passe incorrect.")
        return super().form_invalid(form)


class InscriptionView(FormView):
    template_name = "authentication/inscription.html"
    form_class = InscriptionForm
    success_url = reverse_lazy("flux:flux_view")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)