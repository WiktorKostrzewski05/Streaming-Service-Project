# watchY urls
from django.contrib import admin
from django.urls import path, include
from adminplus.sites import AdminSitePlus
from django.conf import settings
from django.conf.urls.static import static
from . import views

admin.site = AdminSitePlus()
admin.sites.site = admin.site  # extra line
admin.autodiscover()

urlpatterns = [
    path("update_server/", views.update, name="update"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('', include('pages.urls')),
    path('subscribe/', include('subscription.urls')),
    path('media/', include('mediaApp.urls')),
    path('rating/', include('Ratings_Review.urls')),
    path('search/', include('search_app.urls')),
    path('support/', include('customerSupport.urls')),
    path('admin/analysis/', include('data_analyse.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
