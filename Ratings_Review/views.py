from django.shortcuts import render, get_object_or_404, redirect
from .models import ReviewRating
from .forms import ReviewForm
from mediaApp.models import Content
# Create your views here.


def submit_review(request, content_id):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                print(content_id)
                print(request.user.id)
                review = ReviewRating.objects.get(
                    user_id=request.user.id, Content=content_id)
                review.rating = form.cleaned_data['rating']
                review.review = form.cleaned_data['review']
                review.title = form.cleaned_data['title']
                review.save()
                return redirect(url)
            except ReviewRating.DoesNotExist:
                contetnObj = Content.objects.get(id=content_id)
                print(form.cleaned_data['rating'])
                data = ReviewRating.objects.create(
                    user=request.user, Content=contetnObj, rating=form.cleaned_data['rating'], review=form.cleaned_data['review'], title=form.cleaned_data['title'])
                print(data)
                data.save()
                return redirect(url)
