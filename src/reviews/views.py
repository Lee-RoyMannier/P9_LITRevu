from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, View

from reviews.forms import TicketForm, ReviewForm


# Create your views here.
class CreateTicketView(LoginRequiredMixin, FormView):
    template_name = "reviews/ticket_form.html"
    form_class = TicketForm
    success_url = reverse_lazy("flux:flux_view")

    def form_valid(self, form):
        ticket = form.save(commit=False)
        ticket.user = self.request.user
        ticket.save()
        return super().form_valid(form)


class CreateReviewView(LoginRequiredMixin, View):
    template_name = "reviews/review_form.html"
    success_url = reverse_lazy("flux:flux_view")

    def get(self, request):
        review_form = ReviewForm()
        ticket_form = TicketForm()
        context = {
            "ticket": ticket_form,
            "review": review_form,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)

        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket_obj = ticket_form.save(commit=False)
            ticket_obj.user = self.request.user
            ticket_obj.save()
            review_obj = review_form.save(commit=False)
            review_obj.ticket = ticket_obj
            review_obj.save()

            context = {
                "ticket": ticket_obj,
                "review": review_obj,
            }

            return render(self.request, self.template_name, context=context)

