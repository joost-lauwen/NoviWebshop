from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime

from noviwebshopapp.models import UserProfileInfo
from noviwebshopapp.models import Painting
from noviwebshopapp.models import Order

# Class that defines the form to upload/update a painting.
class PaintingForm(forms.ModelForm):

    class Meta():
        model = Painting
        fields = ('name', 'description', 'image', 'price')

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Naam'
        self.fields['description'].label = 'Beschrijving'
        self.fields['image'].label = 'Afbeelding'
        self.fields['price'].label = 'Prijs'

# Class that defines the form to hire a painting.
class HirePaintingForm(forms.ModelForm):

    class Meta():
        model = Painting
        fields = ('rented_from', 'rented_till')

        widgets = {
            'rented_from':forms.SelectDateWidget(empty_label=("Jaar", "Maand", "Dag"), attrs={'class':'form-control'}),
            'rented_till':forms.SelectDateWidget(empty_label=("Jaar", "Maand", "Dag"), attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rented_from'].label = 'Huren van'
        self.fields['rented_till'].label = 'Huren tot'

# Class that defines the form to create a new user.
class UserSignUpForm(UserCreationForm):

    class Meta():
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Gebruikersnaam'
        self.fields['email'].label = 'Email adres'
        self.fields['first_name'].label = 'Voornaam'
        self.fields['last_name'].label = 'Achternaam'
        self.fields['password1'].label = 'Wachtwoord'
        self.fields['password2'].label = 'Wachtwoord herhalen'
