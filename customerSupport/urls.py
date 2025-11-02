from django.urls import path
from . import views

urlpatterns = [
    path('',views.SupportPageView, name='supportPage'),
    path('submit/',views.SubmitSupportRequest, name='submitSupportRequest'),
    path('view/<uuid:request_id>/', views.ViewSupportRequest, name='viewSupportTicket'),
]
