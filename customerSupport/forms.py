from django import forms
from .models import SupportRequest

class SupportRequestForm(forms.ModelForm):
    class Meta:
        model = SupportRequest
        fields = ['req_subject','req_category', 'req_description']
        widgets = {
          'req_subject': forms.Textarea(attrs={'rows':1}),
        }