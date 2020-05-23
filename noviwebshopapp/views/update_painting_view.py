from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from noviwebshopapp.models.painting import Painting
from noviwebshopapp.forms import PaintingForm, HirePaintingForm

class UpdatePaintingView(LoginRequiredMixin, UpdateView):

    login_url = '/login'
    redirect_field_name = 'noviwebshopapp/painting_detail.html'
    model = Painting

    def get_form_class(self):
        if self.request.user.groups.filter(name='Teachers').exists():
            return PaintingForm
        else:
            return HirePaintingForm

    def form_valid(self, form):
        if self.request.user.groups.filter(name='Teachers').exists():
            return super(UpdatePaintingView, self).form_valid(form)
        else:
            form.instance.rented_by = self.request.user
            form.instance.available = False
            return super(UpdatePaintingView, self).form_valid(form)
