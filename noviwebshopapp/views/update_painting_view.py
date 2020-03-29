from django.views.generic import UpdateView
from noviwebshopapp.models.painting import Painting

class UpdatePaintingView(UpdateView):
    fields = ('name', 'description', 'image', 'price')
    model = Painting

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super(UpdatePaintingView, self).form_valid(form)