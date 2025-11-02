from django.shortcuts import render
from django.shortcuts import render
from .models import Profile, WatchedMedia, Recommendation

# Create your views here.

def recommend_content(user):
    profile = Profile.objects.get(user=user)
    favorite_genres = profile.fav_genre.all()
    watched_media = WatchedMedia.objects.filter(user=user, media_completed=True)
    recommended_content = Content.objects.filter(con_genre__in=favorite_genres)
    recommended_content = recommended_content.exclude(id__in=[wm.media.id for wm in watched_media])
    return recommended_content

def recommendation_view(request):
    user = request.user
    recommended_content = recommend_content(user)
    context = {'recommended_content': recommended_content}
    return render(request, 'recommendation.html', context)
