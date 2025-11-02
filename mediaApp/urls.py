from django.urls import path
from . import views
from .views import CreateContentView, EditContentView, AddMediaFiles, EditMediaFiles, AddMediaView, EditMediaView

app_name = 'mediaApp'

urlpatterns = [
    path('all/', views.AllMediaView, name='allMedia'),
    path('view/<uuid:content_id>/', views.viewMedia, name='view_media'),
    path('view/<uuid:content_id>/<uuid:media_id>/', views.viewMediaPlayer, name='view_media_player'),
    path('add_content/',CreateContentView.as_view(),name="add_content"),
    path('edit_content/<uuid:pk>/', EditContentView.as_view(), name='edit_content'),
    path('delete_content/<uuid:pk>/', views.DeleteContent, name='delete_content'),
    path('add_media_file/',AddMediaFiles.as_view(),name="add_media_file"),
    path('edit_media_file/<uuid:pk>/', EditMediaFiles.as_view(), name='edit_media_file'),
    path('add_media/', AddMediaView.as_view(), name='add_media'),
    path('edit_media/<uuid:pk>/', EditMediaView.as_view(), name='edit_media'),
    path('delete_media/<uuid:pk>/', views.DeleteMedia, name='delete_media'),

    #path('filetest/', views.UploadFile.as_view(), name='FileUpload'),
]