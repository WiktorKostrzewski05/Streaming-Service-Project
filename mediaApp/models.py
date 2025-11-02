from django.db import models
import uuid
from django.urls import reverse
#from .custom_storage import CustomFileStorage
import requests


class Genre(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    type_genre = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ('type_genre',)
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.type_genre


class MediaFile(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    file_title = models.TextField(null=False, blank=False, max_length=250)
    file_url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ('file_title',)
        verbose_name = 'mediaFile'
        verbose_name_plural = 'mediaFiles'

    def __str__(self):
        return self.file_title

class Content(models.Model):
    CHOICES = (
        ('show', 'Show'),
        ('movie', 'Movie'),
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    con_available = models.BooleanField(default=True)
    con_title = models.TextField(max_length=250, unique=True)
    con_description = models.TextField(blank=True)
    con_genre = models.ForeignKey(Genre,blank=True,null=True, on_delete=models.CASCADE)
    con_released = models.DateField(blank=True, null=True)
    con_upload_date = models.DateField(blank=True, null=True)
    con_withdrawal_date = models.DateField(null=True, blank=True)
    con_icon = models.URLField(null=True, blank=True)
    con_trailer = models.ForeignKey(MediaFile,blank=True,null=True, on_delete=models.CASCADE)
    con_type = models.CharField(
        max_length=6, choices=CHOICES, default='movie')

    class Meta:
        ordering = ('con_title',)
        verbose_name = 'content'
        verbose_name_plural = 'content'

    def __str__(self):
        return self.con_title + " | " + self.con_type


class Media(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    med_title = models.TextField(null=False, blank=False, max_length=250 )
    med_description = models.TextField(null=True, blank=True, max_length=500)
    med_file = models.ForeignKey(MediaFile,blank=True,null=True, on_delete=models.CASCADE)
    med_pill = models.TextField(null=True, blank=True, max_length=50)
    med_content = models.ForeignKey(Content,blank=True,null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('med_title',)
        verbose_name = 'media'
        verbose_name_plural = 'media'
    
    def __str__(self):
        return self.med_title




class ContentRow(models.Model):
    CHOICES = (
        ('show', 'Show'),
        ('movie', 'Movie'),
        ('allContent', 'All Content'),
    )
    row_title = models.TextField(max_length=50, unique=True)
    row_type = models.CharField(
        max_length=10, choices=CHOICES, default='allContent')
    row_position = models.IntegerField(null=True, blank=True)
    row_genre = models.ForeignKey(Genre,blank=True,null=True, on_delete=models.CASCADE)
    row_director = models.CharField(null=True, blank=True, max_length=50)
    row_content = models.ManyToManyField(Content, blank=True)
    


class Featured(models.Model):
    feat_title = models.TextField(max_length=50, null=True, blank=True)
    feat_position = models.IntegerField(null=True, blank=True)
    feat_content = models.OneToOneField(
        Content, on_delete=models.CASCADE, blank=True, )

    class Meta:
        verbose_name = 'featured'
        verbose_name_plural = 'featured'
