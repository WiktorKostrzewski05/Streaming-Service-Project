from django.urls import path
from . import views
urlpatterns = [
    path('submit_review/<uuid:content_id>/', views.submit_review, name='submited_review'),
]
