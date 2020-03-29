from django.views.generic import CreateView
from noviwebshopapp.models.painting import Painting

class UploadPaintingView(CreateView):
    fields = ('name', 'description', 'image', 'price')
    model = Painting

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(UploadPaintingView, self).form_valid(form)
        