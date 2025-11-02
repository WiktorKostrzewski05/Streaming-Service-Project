from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
import uuid



class subscription(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    user = models.OneToOneField(
        get_user_model(),
        null=True,
        on_delete=models.CASCADE,
    )
    startDate = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=False)
    customerId = models.TextField(null=True, blank=True, max_length=255)

    class Meta:
        db_table = 'subscription'
        ordering = ['-user']

    def __str__(self):
        return str(self.id)


def create_sub(sender, instance, created, **kwargs):
    if created:
        user_profile = subscription(user=instance)
        user_profile.save()


post_save.connect(create_sub, sender=get_user_model())
