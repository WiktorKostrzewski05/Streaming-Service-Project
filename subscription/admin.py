from django.contrib import admin
from .models import subscription



class SubAdmin(admin.ModelAdmin):
    list_display = ['user', 'startDate', 'active']
    list_editable = ['startDate','active']

admin.site.register(subscription, SubAdmin)
