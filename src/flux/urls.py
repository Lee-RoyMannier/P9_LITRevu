from django.urls import path
from flux.views import FluxView


app_name = 'flux'
urlpatterns = [
    path("", FluxView.as_view(), name="flux_view"),
]