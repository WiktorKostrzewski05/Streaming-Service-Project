from .models import Genre, Content, ContentRow, Featured, Media, MediaFile
from django.shortcuts import render, get_object_or_404
from django.contrib import admin

# mediaApp admin.py


class ContentAdmin(admin.ModelAdmin):
    list_display = ['con_title', 'con_description','con_type', 'con_available']
    list_editable = ['con_available','con_type']
    # newest_release = 'con_released'
    list_filter = [
         "con_type",
    ]
    search_fields = (
        "con_type",
        "con_title",
    )
    list_per_page = 30


admin.site.register(Content, ContentAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ['type_genre']
    search_fields = ['type_genre']
    list_per_page = 25


admin.site.register(Genre, GenreAdmin)


class MediaRowsAdmin(admin.ModelAdmin):
    list_display = ['row_title','row_position','row_type']
    list_editable = ['row_position','row_type']
    list_filter = [
         "row_type",
    ]
    search_fields = (
        "row_type",
        "row_title",
    )
    list_per_page = 30
    ordering = ('row_position',)


admin.site.register(ContentRow, MediaRowsAdmin)


class FeaturedAdmin(admin.ModelAdmin):
    list_display = ['feat_title', 'feat_content']
    # newest_release = 'con_released'
    list_per_page = 15


admin.site.register(Featured, FeaturedAdmin)


class MediaAdmin(admin.ModelAdmin):
    list_display = ['med_title','med_description','med_pill','med_content']
    list_filter = [
         "med_title",
         "med_pill",
    ]
    search_fields = (
        "med_title",
         "med_pill",
    )
    list_per_page = 30



admin.site.register(Media, MediaAdmin)


def ContentManager(requests):
    mediaFile = MediaFile.objects.all()
    media = Media.objects.all()
    content = Content.objects.all()
    return render(requests, 'contentManager.html', {'mediaFile': mediaFile, 'content': content, 'media': media})


admin.site.register_view('mediaApp/contentManager', view=ContentManager,
                         urlname='contentManager', name='Content Manager')


class MediaFileAdmin(admin.ModelAdmin):
    list_display = ['file_title']
    list_per_page = 15


admin.site.register(MediaFile, MediaFileAdmin)
