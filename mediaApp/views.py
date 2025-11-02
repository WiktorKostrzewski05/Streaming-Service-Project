from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView
from django.conf import settings
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from .models import Genre, Content, ContentRow, Featured, Media
from subscription.models import subscription
from django.db.models import Avg
from .models import Content, MediaFile, Media
from .forms import ContentForm, MediaFileForm, MediaForm
from suggestions.models import Recommendation
import stripe

adminAppUrl = '/admin/mediaApp/contentManager'
stripe.api_key = settings.STRIPE_SECRET_KEY


def AllMediaView(request):
    mediaRows = ContentRow.objects.all()
    featured = Featured.objects.all()
    rows = []
    types = ['all', 'movie', 'show']
    features = []

    for row in mediaRows:
        contentList = []
        rowPos = 999
        print(row.row_position)
        rowType = row.row_type

        if row.row_position != None:
            rowPos = row.row_position
        for content in row.row_content.all():
            contentList.append(content)

        allContentInGenre = Content.objects.filter(con_genre=row.row_genre)
        print(allContentInGenre)
        for genreContent in allContentInGenre:
            contentList.append(genreContent)

        if len(contentList) > 0:
            rows.append(
                {"rowInfo": row, "contentList": contentList, "rowPostion": rowPos, "rowType": rowType})

    for feat in featured:
        content = feat.feat_content
        featPos = 999
        if feat.feat_position != None:
            featPos = feat.feat_position

        features.append(
            {"featureInfo": feat, "content": content, "featurePosition": featPos, "first": ""})

    rows.sort(key=lambda x: x["rowPostion"])
    features.sort(key=lambda x: x["featurePosition"])

    if len(features) > 0:
        features[0]["first"] = "active"

    return render(request, 'allMedia.html', {'Rows': rows, 'Featured': features})


def viewMedia(request, content_id):
    content = get_object_or_404(Content, id=content_id)
    typ = content.con_type
    average_rating = content.reviewrating_set.aggregate(Avg('rating'))[
        'rating__avg']
    media = []
    movie = []
    pillList = []
    if typ == "movie":
        movie = Media.objects.filter(med_content=content_id, med_title="Movie")
        if len(movie) > 0:
            movie = movie[0]

    tempMedia = Media.objects.filter(
        med_content=content_id).exclude(med_title="Movie")

    pills = []
    for med in tempMedia:
        pill = med.med_pill
        if med.med_pill == "":
            pill = "Trailers and More"
        if pill not in pills:
            if med.med_title != "Movie":
                pills.append(pill)
        titleOrder = pill + med.med_title
        media.append({"Pill": pill, "TitleOrder": titleOrder, "Info": med})

    for i, pill in enumerate(pills):
        tempMediaList = [med for med in media if med["Pill"] == pill]
        tempMediaList.sort(key=lambda x: x["TitleOrder"])
        pillList.append({"Title": pill, "Id": i, "Media": tempMediaList})

    pills.sort(key=lambda x: x[0])

    allowedPlay = False

    if request.user.is_authenticated:
        sub = subscription.objects.get(user=request.user)
        customerId = sub.customerId
        print(sub.customerId)
        if customerId != None:
            subscriptionInfo = (stripe.Subscription.retrieve(customerId))
            subStatus = subscriptionInfo["items"]["data"][0]["plan"]["active"]
            if subStatus == True:
                allowedPlay = True
    return render(request, 'viewMedia.html', {'Content': content, 'PillList': pillList, 'Movie': movie, 'Type': typ, 'AllowedPlay': allowedPlay, 'AverageRating': average_rating})


def viewMediaPlayer(request, content_id, media_id):
    media = get_object_or_404(Media, id=media_id)
    allowedPlay = False

    if request.user.is_authenticated:
        allowedPlay = True

    source = ""
    if media.med_file:
        source = media.med_file.file_url

    print("AllowedPlay", allowedPlay)
    print(request.user)
    return render(request, 'viewMediaPlayer.html', {'Source': source, 'AllowedPlay': allowedPlay})


class CreateContentView(CreateView):
    model = Content
    form_class = ContentForm
    template_name = 'add_content.html'
    success_url = adminAppUrl


class EditContentView(UpdateView):
    model = Content
    form_class = ContentForm
    template_name = 'edit_content.html'
    success_url = adminAppUrl


def DeleteContent(request, pk):
    cont = Content.objects.get(id=pk)
    cont.delete()
    return redirect(adminAppUrl)


class AddMediaFiles(CreateView):
    model = MediaFile
    form_class = MediaFileForm
    template_name = 'add_mediaFile.html'
    success_url = adminAppUrl


class EditMediaFiles(UpdateView):
    model = MediaFile
    form_class = MediaFileForm
    template_name = 'edit_mediaFile.html'
    success_url = adminAppUrl


class AddMediaView(CreateView):
    model = Media
    form_class = MediaForm
    template_name = 'add_media.html'
    success_url = adminAppUrl


class EditMediaView(UpdateView):
    model = Media
    form_class = MediaForm
    template_name = 'edit_media.html'
    success_url = adminAppUrl


def DeleteMedia(request, pk):
    cont = Media.objects.get(id=pk)
    print(cont)
    cont.delete()
    return redirect(adminAppUrl)
