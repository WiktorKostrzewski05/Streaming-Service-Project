from django.urls import path
from . import views

urlpatterns = [
    path('subs_analysis/', views.subscription_analysis, name='subs_analysis'),
    path('top_rating_analysis/', views.top_rated, name='top_rated_media'),
]