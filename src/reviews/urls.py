from django.urls import path
from reviews.views import CreateTicketView, CreateReviewView, review_about_ticket, modify_ticket, delete_ticket, modify_review


app_name = "review"
urlpatterns = [
    path("create-ticket/", CreateTicketView.as_view(), name="create_ticket"),
    path("create-review", CreateReviewView.as_view(), name="create_review"),
    path("review/<int:ticket_id>", review_about_ticket, name="review_ticket"),
    path("ticket/<int:ticket_id>", modify_ticket, name="update_ticket"),
    path("ticket/delete/d<int:ticket_id>", delete_ticket, name="delete_ticket"),
    path("review/<int:review_id>/update/", modify_review, name="modify_review"),

]