from django.shortcuts import redirect, render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView
from django.conf import settings
import stripe
from .models import subscription
from datetime import date

stripe.api_key = settings.STRIPE_SECRET_KEY


class SubscribedView(TemplateView):
    template_name = 'subscribed.html'

class UnsubscribedView(TemplateView):
    template_name = 'unsubscribed.html'


def Subscribe(request, total=0):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_total = int(total*100)
    description = 'Watchy'

    subbed = False
    if request.user.is_authenticated:
        email = str(request.user.email)
        try:
            subscriptionDetails = subscription.objects.get(
                user=request.user)
            customerId = subscriptionDetails.customerId
            if customerId != None:
                subscriptionInfo = (stripe.Subscription.retrieve(customerId))
                subActive = subscriptionInfo["items"]["data"][0]["plan"]["active"]
                if subActive == True:
                    subbed = True
        except subscription.DoesNotExist:
            subbed = False

        if request.method == 'POST':
            try:
                try:
                    token = request.POST['stripeToken']
                    email = str(request.user.email)
                    customer = stripe.Customer.create(email=email, source=token)
                    stripeSubscription = stripe.Subscription.create(
                        customer=customer,
                        items=[{"price": "price_1OkqqMKLNSgw8Hh9wab95yaf"}],
                    )
                    try:
                        sub_details = subscription.objects.get(
                            user=request.user,
                        )
                        sub_details.startDate = str(date.today())
                        sub_details.active = True
                        sub_details.customerId = stripeSubscription.id
                        sub_details.save()
                        return redirect('subscribed')

                    except ObjectDoesNotExist:
                        pass

                except stripe.error.CardError as e:
                    return e
            except:    
                if request.POST['type'] == "Unsubscribe":
                    if subbed == True:
                        print(subbed)
                        subscriptionDetails = subscription.objects.get(
                            user=request.user.id)
                        customerId = subscriptionDetails.customerId
                        print(request.POST)
                        stripe.Subscription.cancel(customerId)
                        sub_details = subscription.objects.get(
                            user=request.user,
                        )
                        sub_details.active = False
                        sub_details.customerId = None
                        sub_details.save()
                        return redirect('unsubscribed')

    return render(request, 'subscribe.html', {'total': total, 'data_key': data_key, 'stripe_total': stripe_total, 'description': description, 'subbed': subbed})
