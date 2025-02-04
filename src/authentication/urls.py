from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path
from authentication.views import LoginHomePageView, InscriptionView

app_name = "auth"
urlpatterns = [
    path("", LoginHomePageView.as_view(), name="home_page"),
    path("logout/", LogoutView.as_view(
        next_page=settings.LOGOUT_URL), name="logout"),
    path("inscription/", InscriptionView.as_view(), name="inscription"),
]