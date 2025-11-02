from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import CustomUserCreationForm
from .models import Profile, WatchedMedia
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.utils import timezone

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileEditView(UpdateView):
    model = Profile 
    template_name = 'edit_profile.html'
    fields = ['bio', 'fav_actor', 'fav_director', 'fav_genre']

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'user_profile.html'

@require_POST
def pused_media(request, media_id):
    watched_media = get_object_or_404(WatchedMedia, user=request.user, media_id=media_id)
    watched_media.pused_media = timezone.now() - watched_media.last_view_timestamp
    watched_media.save()
    return HttpResponse("Paused")

@require_POST
def resume_media(request, media_id):
    watched_media = get_object_or_404(WatchedMedia, user=request.user, media_id=media_id)
    watched_media.last_view_timestamp = timezone.now()
    watched_media.save()
    return HttpResponse("Resuming")