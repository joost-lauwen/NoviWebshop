from django.views.generic import ListView
from noviwebshopapp.models.painting import Painting

class IndexListView(ListView):
    context_object_name = 'painting_list'
    model = Painting
    template_name = 'noviwebshopapp/index.html'

    def get_queryset(self):
        return Painting.objects.filter(available=True).order_by('-date_added')
