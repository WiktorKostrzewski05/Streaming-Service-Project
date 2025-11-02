from django.db import models
from django.contrib.auth import get_user_model
from mediaApp.models import Content, Genre
from users.models import WatchedMedia

# Create your models here.

class Recommendation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    recommended_media = models.ForeignKey(Content, on_delete=models.CASCADE)

