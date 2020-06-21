from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from noviwebshopapp.models.painting import Painting

# Class that handles the deletion of a painting. Required to be loged in.
class DeletePaintingView(LoginRequiredMixin, DeleteView):

    login_url = '/login'
    redirect_field_name = 'noviwebshopapp/painting_detail.html'

    model = Painting
    success_url = reverse_lazy("noviwebshopapp:index")
