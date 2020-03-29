from django import forms
from django.contrib.auth.models import User
from noviwebshopapp.models import UserProfileInfo
from noviwebshopapp.models import Painting

class PaintingForm(forms.ModelForm):
    
    class Meta():
        model = Painting
        fields = ('name', 'description', 'image', 'price')

        widgets = {
            'name':forms.TextInput(attrs={'class':'textinputclass'}),
            'description':forms.Textarea(attrs={'class':'textareaclass'}),
        }

class NewUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('role', 'profile_pic')
        