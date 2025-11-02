from django import forms
from .models import Content, MediaFile, Media


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = "__all__"
        widgets = {
            'con_upload_date': forms.TextInput(attrs={'type': 'date'}),
            'con_released': forms.TextInput(attrs={'type': 'date'}),
            'con_withdrawal_date': forms.TextInput(attrs={'type': 'date'}),
            'con_title': forms.Textarea(attrs={'rows': 1}),
            'con_description': forms.Textarea(attrs={'rows': 2}),

        }

class MediaFileForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ["file_title"]
        widgets = {'file_title': forms.Textarea(attrs={'rows': 1})}

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = "__all__"
        widgets = {'med_title': forms.Textarea(attrs={'rows': 1}),
                   'med_pill': forms.Textarea(attrs={'rows': 1}),
                   'med_description': forms.Textarea(attrs={'rows': 1}),}