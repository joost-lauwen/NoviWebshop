from django.views.generic import ListView
from noviwebshopapp.models.painting import Painting

# Class that handles the homepage.
class IndexListView(ListView):
    context_object_name = 'painting_list'
    model = Painting
    template_name = 'noviwebshopapp/index.html'

# Function to filter Paintings if available
    def get_queryset(self):
        return Painting.objects.filter(available=True).order_by('-date_added')
