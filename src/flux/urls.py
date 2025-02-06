from django.urls import path
from flux.views import FluxView, DisplayMyPost


app_name = 'flux'
urlpatterns = [
    path("", FluxView.as_view(), name="flux_view"),
    path("posts/", DisplayMyPost.as_view(), name="my_posts"),
]