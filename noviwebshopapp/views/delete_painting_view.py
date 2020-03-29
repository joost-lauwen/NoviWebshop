from django.views.generic import DeleteView
from django.urls import reverse_lazy
from noviwebshopapp.models.painting import Painting

class DeletePaintingView(DeleteView):
    model = Painting
    success_url = reverse_lazy("noviwebshopapp:index")
    