from django.urls import path
from . import views

urlpatterns = [
    path('', views.Subscribe, name='FlowPro'),
    path('subscribed/', views.SubscribedView.as_view(), name='subscribed'),
    path('unsubscribed/', views.UnsubscribedView.as_view(), name='unsubscribed'),

]
