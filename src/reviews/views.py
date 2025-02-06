from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, View
from reviews.models import Ticket, Review
from reviews.forms import TicketForm, ReviewForm


# Create your views here.
class CreateTicketView(LoginRequiredMixin, FormView):
    template_name = "reviews/ticket_form.html"
    form_class = TicketForm
    success_url = reverse_lazy("flux:flux_view")

    def form_valid(self, form):
        ticket = form.save(commit=False)
        ticket.user = self.request.user
        if ticket.image:
            ticket.image = self.request.FILES['image']
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
            ticket_obj.user = request.user
            if ticket_obj.image:
                ticket_obj.image = request.FILES['image']
            ticket_obj.save()
            review_obj = review_form.save(commit=False)
            review_obj.user = request.user
            review_obj.ticket = ticket_obj
            review_obj.save()

            return redirect(self.success_url)

        context = {
                "ticket": ticket_form,
                "review": review_form,
            }

        return render(request, self.template_name, context=context)



def review_about_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    review_form = ReviewForm(instance=ticket)
    success_url = reverse_lazy("flux:flux_view")

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_obj = review_form.save(commit=False)
            review_obj.ticket = ticket
            review_obj.user = request.user
            review_obj.save()

            return redirect(success_url)
    context = {
        "ticket": ticket,
        "review_form": review_form,
    }
    return render(request, "reviews/review_about_ticket.html", context=context)


def modify_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket_form = TicketForm(instance=ticket)

    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES, instance=ticket)
        if ticket_form.is_valid():
            ticket_obj = ticket_form.save(commit=False)
            ticket_obj.title = ticket_form.cleaned_data["title"]
            ticket_obj.description = ticket_form.cleaned_data["description"]
            ticket_obj.image = ticket_form.cleaned_data["image"]
            ticket_form.save()

            return redirect("flux:my_posts")

    context = {
        "form": ticket_form,
        "ticket": ticket,
    }

    return render(request, "reviews/ticket_updating.html", context=context)


def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)

    if request.method == "POST":
        ticket.delete()

        return redirect("flux:my_posts")

    return render(request, "reviews/delete_ticket.html")
