from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from reviews.models import Ticket, Review


class FluxView(LoginRequiredMixin, TemplateView):
    template_name = 'flux/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tickets"] = Ticket.objects.all()

        return context
