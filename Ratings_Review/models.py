from django.db import models
from mediaApp.models import Content
from users.models import Profile
from django.contrib.auth import get_user_model
import uuid


# Create your models here.
class ReviewRating(models.Model):
    
    Content = models.ForeignKey(Content, on_delete=models.CASCADE)
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=1000, blank=True)
    rating = models.FloatField()
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

