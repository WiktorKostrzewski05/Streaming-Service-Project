from django.contrib import admin
from .models import SupportRequest



class SupportRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'req_subject', 'req_date_requested','req_category','req_status']
    list_editable = ['req_category','req_status']
    list_filter = [
         "req_status",
         "req_category",
         "req_date_requested"
    ]
    search_fields = (
        "req_subject",
         "req_subject",

    )
    list_per_page = 30


admin.site.register(SupportRequest, SupportRequestAdmin)