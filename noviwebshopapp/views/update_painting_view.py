from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from noviwebshopapp.models.painting import Painting
from noviwebshopapp.forms import PaintingForm

class UpdatePaintingView(LoginRequiredMixin, UpdateView):
    
    login_url = '/login'
    redirect_field_name = 'noviwebshopapp/painting_detail.html'

    # fields = ('name', 'description', 'image', 'price')
    model = Painting
    form_class = PaintingForm

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super(UpdatePaintingView, self).form_valid(form)