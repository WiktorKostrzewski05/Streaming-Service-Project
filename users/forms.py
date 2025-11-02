from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields+('email','date_of_birth')
        widgets = {
            'date_of_birth': forms.TextInput(attrs={'type': 'date'}),

        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields