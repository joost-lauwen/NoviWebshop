from django.views.generic import ListView
from django.contrib.auth.models import User, Group
from noviwebshopapp.models.painting import Painting

# Class that handles the paintings overview based on loged in user.
class UserPaintingsListView(ListView):
    context_object_name = 'painting_list'
    model = Painting
    template_name = 'noviwebshopapp/user_paintings_list.html'

# Function to determine if the filter must filter on author or on tenant.
    def get_queryset(self):
        if self.request.user.groups.filter(name='Teachers').exists():
            return Painting.objects.filter(author=self.request.user).order_by('-date_added')
        else:
            return Painting.objects.filter(rented_by=self.request.user).order_by('-date_added')
