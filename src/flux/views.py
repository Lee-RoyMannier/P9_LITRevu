from itertools import chain

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, CharField, Value
from django.shortcuts import render
from django.views.generic import TemplateView
from reviews.models import Ticket, Review


class FluxView(LoginRequiredMixin, TemplateView):
    template_name = 'flux/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tickets"] = Ticket.objects.filter(
            Q(user=self.request.user) |
            Q(user__in=self.request.user.follows.all())
        ).annotate(content_type=Value('TICKET', CharField()))

        context["reviews"] = Review.objects.filter(
            Q(user=self.request.user) |
            Q(user__in=self.request.user.follows.all()) |
            Q(ticket__user=self.request.user)
        ).annotate(content_type=Value('REVIEW', CharField()))

        context["rating_range"] = list(range(1,6))
        context["all_flux"] = sorted(chain(context["tickets"], context["reviews"]),
                                     key=lambda instance: instance.time_created, reverse=True)
        return context


class DisplayMyPost(LoginRequiredMixin, TemplateView):
    template_name = 'flux/posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tickets"] = Ticket.objects.filter(user=self.request.user)
        context["reviews"] = Review.objects.filter(user=self.request.user)
        context["rating_range"] = list(range(1,6))
        context["all_flux"] = sorted(chain(context["tickets"], context["reviews"]),
                                     key=lambda instance: instance.time_created, reverse=True)
        return context

