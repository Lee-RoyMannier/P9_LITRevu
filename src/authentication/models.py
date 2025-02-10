from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
        Custom user model who have same attributes from AbstractUser
        Whe give him a role :
            - CREATOR
            - SUBSCRIBER
        A Creator have the power of delete a ticket or a review ticket
    """
    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"
    USER_ROLE = (
        (CREATOR, "Creator"),
        (SUBSCRIBER, "Subscriber"),
    )

    role = models.CharField(max_length=30, choices=USER_ROLE, default=SUBSCRIBER, verbose_name="User_role")
    follows = models.ManyToManyField(
        'self', through='subscriber.UserFollows', related_name='is_followed_by', symmetrical=False
    )
