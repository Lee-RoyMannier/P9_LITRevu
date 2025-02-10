from django.urls import path
from subscriber.views import follow_page, UnfollowUserView


app_name = "follow"
urlpatterns = [
    path("", follow_page, name="follow"),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),

]