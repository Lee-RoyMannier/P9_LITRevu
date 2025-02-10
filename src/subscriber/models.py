from django.conf import settings
from django.db import models


# Create your models here.
class UserFollows(models.Model):
    class Meta:
        unique_together = (('user', 'followed_by'),)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')