from django.views.generic import DetailView
from noviwebshopapp.models.painting import Painting

class PaintingDetailView(DetailView):
    model = Painting
    context_object_name = 'painting_detail'
    template_name = 'noviwebshopapp/painting_detail.html'
