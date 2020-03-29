from django.views.generic import ListView
from noviwebshopapp.models.painting import Painting

class IndexListView(ListView):
    context_object_name = 'painting_list'
    model = Painting
    queryset = Painting.objects.exclude(available=False)
    template_name = 'noviwebshopapp/index.html'
