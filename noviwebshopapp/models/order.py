from django.db import models
from django.contrib.auth.models import User
from .painting import Painting

# Model for the order class. This model stores the transactions.

class Order(models.Model):
    order = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="Order-test")
    painting = models.ForeignKey(Painting, on_delete=models.SET_NULL, related_name="order_painting", null=True)
    transaction_date = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(decimal_places=2, max_digits=9999, default=0.00)
    payment_status = models.BooleanField(default=False)
    tenant = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='tenant_painting', blank=True)

    def __str__(self):
        return self.name
