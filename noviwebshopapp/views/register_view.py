from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from noviwebshopapp.forms import UserSignUpForm

class SignUp(FormView):
    form_class = UserSignUpForm
    success_url = reverse_lazy("noviwebshopapp:index")
    template_name = "noviwebshopapp/registration.html"

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']

        user = authenticate(username=username,password=password)
        login(self.request, user)

        return HttpResponseRedirect(self.get_success_url())
