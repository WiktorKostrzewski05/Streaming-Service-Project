from django.contrib import admin
from .views import admin_analysis
# Register your models here.
admin.site.register_view('analysis/data_analysis', view=admin_analysis,
                         urlname='admin_analysis', name='Data Analysis')
