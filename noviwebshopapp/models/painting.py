from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

class Painting(models.Model):
    painting= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_painting')
    image = models.ImageField(upload_to='paintings')
    price = models.DecimalField(decimal_places=2, max_digits=9999)
    available = models.BooleanField(default=True)
    rented_from = models.DateField(null=True, blank=True)
    rented_till = models.DateField(null=True, blank=True)
    rented_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='renter_painting', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("noviwebshopapp:painting_detail", kwargs={"pk": self.pk})

    @property
    def is_overdue(self):
        if self.rented_till and date.today() > self.rented_till:
            return True
        return False

    def get_rented_months(self, rented_till, rented_from):
        return (rented_till.year - rented_from.year) * 12 + rented_till.month - rented_from.month
