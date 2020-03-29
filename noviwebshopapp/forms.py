from django import forms
from django.core import validators
from django.contrib.auth.models import User
from noviwebshopapp.models import UserProfileInfo


class PaintingForm(forms.ModelForm):
    name = forms.CharField(max_length=50, 
                            required=True)
    email = forms.EmailField()
    description = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

class NewUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('role', 'profile_pic')
        