from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse 
from django.db.models.signals import post_save
from django.utils import timezone
from django.conf import settings
from mediaApp.models import Content

# Create your models here.

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=False )

class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key = True,
    )
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.CharField(default=('No Bio added'), max_length=2555,blank=True, null=True)
    subscription_status = models.CharField(default=('None'), max_length=50,blank=True, null=True)
    fav_actor = models.CharField(default=('No favorite actor added'), max_length=2555,blank=True, null=True)
    fav_director = models.CharField(default=('No favorite director added'), max_length=2555,blank=True, null=True)
    fav_genre = models.CharField(default=('No favorite genre added'), max_length=2555,blank=True, null=True)
    
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('view_profile', args=[str(self.user.id)])

def create_prof(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_prof, sender=get_user_model())

class WatchedMedia(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        media_type = models.CharField(max_length=20)
        type_genre = models.CharField(max_length=15)
        media_id = models.UUIDField()
        last_view_timestamp = models.DateTimeField(default=timezone.now)
        media_paused = models.DurationField(null=True, blank=True)
        media_completed = models.BooleanField(default=False)

class Meta:
    unique_together = ('user', 'media_id')

    def __str__(self):
        if self.media_type == 'movie':
            return self.media.mov_title if self.media else "Movie not found"
        elif self.media_type == 'show':
            return self.media.show_title if self.media else "Show not found"
        else:
            return "Unknown media type"