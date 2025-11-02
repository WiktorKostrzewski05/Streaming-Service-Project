from django.shortcuts import render, redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
import json
import matplotlib.pyplot as plt
from django.conf import settings
from subscription.models import subscription
from Ratings_Review.models import ReviewRating
from mediaApp.models import Content
import os

# @login_required


def admin_analysis(request):
    if request.user.is_superuser:
        subDataActive = subscription.objects.filter(active=True).values()
        subDataInActive = subscription.objects.filter(active=False).values()
        plot_data = {'with_subs': len(subDataActive), 'without_subs': len(subDataInActive)}

        total_ratings_per_title = ReviewRating.objects.values('Content__con_title').annotate(num_ratings=Count('pk'))
        print("Total rating per title")
        print(total_ratings_per_title)
        print("******************************")

        titles = [item['Content__con_title'] for item in total_ratings_per_title]
        print("Titles")
        print(titles)
        print("******************************")
        
        total_ratings = [item['num_ratings'] for item in total_ratings_per_title]
        print("Total rating")
        print(total_ratings)
        print("******************************")

        plot_data_r = {
            "titles": titles,
            "ratings": total_ratings,
        }
        print("Plot data r")
        print(plot_data_r)
        print("****************End***************")

        # rating_file_path = os.path.join(settings.BASE_DIR, 'data_analyse', 'rate.json')

        # try:
        #     with open(rating_file_path, 'r') as r_file:
        #         rated_data = json.load(r_file)
        # except FileNotFoundError:
        #     return HttpResponseServerError("Rating data file not found")
        
        # total_ratings_per_title = {}

        # for rating in rated_data:
        #     status = rating.get("status", True)
        #     title_id = rating.get("fields", {}).get("Content", "")
            
        #     if title_id:
        #         try:
        #             content_obj = Content.objects.get(id=title_id)
        #             title = content_obj.con_title

        #             total_ratings_per_title[title] = total_ratings_per_title.get(title, 0) + 1

        #         except Content.DoesNotExist:
        #             pass

        # titles = list(total_ratings_per_title.keys())
        # total_ratings = list(total_ratings_per_title.values())

        # plot_data_r = {
        #     "titles": titles,
        #     "ratings": total_ratings,
        # }


        context = {'sub_data': json.dumps(plot_data),'rating_data': json.dumps(plot_data_r)}
        return render(request, 'base_admin.html', context)

    else:
        return redirect("home")

def subscription_analysis(request):
    if request.user.is_superuser:
       
        return render(request, 'subs_analysis.html')
    else:
        return redirect("home")


def top_rated(request):
    if request.user.is_superuser:
        
        return render(request, 'top_rating_analysis.html')
    else:
        return redirect("home")

