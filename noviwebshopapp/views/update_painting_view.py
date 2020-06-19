from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from noviwebshopapp.models.painting import Painting
from noviwebshopapp.models.order import Order
from noviwebshopapp.forms import PaintingForm, HirePaintingForm
from datetime import datetime

class UpdatePaintingView(LoginRequiredMixin, UpdateView):

    login_url = '/login'
    redirect_field_name = 'noviwebshopapp/painting_detail.html'
    model = Painting
    context_object_name = 'painting_detail'

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

            order = Order(painting=Painting.objects.get(painting=form.instance.painting),
                            tenant=self.request.user,
                            name=form.instance.name + ' ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                            total_amount=Painting.get_rented_months(Painting.objects.get(painting=form.instance.painting), form.instance.rented_till, form.instance.rented_from) * form.instance.price)
            order.save()

            return super(UpdatePaintingView, self).form_valid(form)
