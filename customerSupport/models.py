from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth import get_user_model


class SupportRequest(models.Model):
    CHOICES = (
        ('subscription','Subscription'),
        ('content','Watch Content'),
        ('watchy_exclusives','WatchY Exclusives'),
        ('account','My Account')

    )
    STATUS = (
        ('new','New'),
        ('in_progress','In Progress'),
        ('stuck','Stuck'),
        ('resolved','Resolved'),
        ('closed_not_resolved','Closed Not Resolved')

    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    req_subject = models.TextField(max_length=30, verbose_name="Subject")
    req_description = models.TextField(max_length=1000, verbose_name="Description")
    req_date_requested = models.DateField(("Date"), auto_now_add=True)
    req_category = models.CharField(
            max_length=17, choices=CHOICES, verbose_name="Category")
    req_status = models.CharField(
            max_length=19, choices=STATUS, default="new", verbose_name="Status")

    class Meta:
        ordering = ('req_date_requested',)
