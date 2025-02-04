from django.urls import path
from reviews.views import CreateTicketView, CreateReviewView


app_name = "review"
urlpatterns = [
    path("create-ticket/", CreateTicketView.as_view(), name="create_ticket"),
    path("create-review", CreateReviewView.as_view(), name="create_review"),
]