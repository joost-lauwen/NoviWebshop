from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from noviwebshopapp.models.painting import Painting
from noviwebshopapp.forms import PaintingForm

class UploadPaintingView(LoginRequiredMixin, CreateView):

    login_url = '/login'
    redirect_field_name = 'noviwebshopapp/painting_detail.html'

    model = Painting
    form_class = PaintingForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(UploadPaintingView, self).form_valid(form)
