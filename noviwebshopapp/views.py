from django.shortcuts import render
# from django.http import HttpResponse
from noviwebshopapp.models import AccesRecord, Painting, Webpage
from . import forms
from noviwebshopapp.forms import NewUserForm

def index(request):
    webpagesList = AccesRecord.objects.order_by('date')
    dateDict = {'access_records':webpagesList}
    return render(request, 'noviwebshopapp/index.html', context=dateDict)

def painting_form_view(request):
    form = forms.PaintingForm()

    if request.method == 'POST':
        form = forms.PaintingForm(request.POST)

        if form.is_valid():
            print("VALIDATIONSUCCES")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Description: "+form.cleaned_data['description'])

    return render(request, 'noviwebshopapp/form_page.html', {'form': form})

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    
    return render(request, 'noviwebshopapp/users.html', {'form':form})