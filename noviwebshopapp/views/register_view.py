from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from noviwebshopapp.forms import NewUserForm, UserProfileInfoForm

def registration(request):

    registered = False 

    if request.method == "POST":
        registration_form = NewUserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if registration_form.is_valid() and profile_form.is_valid():
            
            user = registration_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(registration_form.errors, profile_form.errors)
    
    else: 
        registration_form = NewUserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request, 'noviwebshopapp/registration.html', {'registration_form':registration_form,
                                                                'profile_form':profile_form,
                                                                'registered':registered
                                                                })