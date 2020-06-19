from django.views.generic import DetailView
from noviwebshopapp.models.painting import Painting
from noviwebshopapp.models.order import Order
from datetime import datetime

class PaintingDetailView(DetailView):
    model = Painting
    context_object_name = 'painting_detail'
    template_name = 'noviwebshopapp/painting_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PaintingDetailView, self).get_context_data(**kwargs)
        painting = self.get_object()
        context['order_detail'] = Order.objects.filter(painting=painting).last()

        return context
