from django.db import models
from django.conf import settings

class Player(models.Model):
    """Player model."""
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    nickname = models.CharField(
        max_length=45,
        blank=False,
        null=False,
        unique=True,
    )
    experience = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.nickname}"
