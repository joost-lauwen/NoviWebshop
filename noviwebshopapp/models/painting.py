from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Painting(models.Model):
    painting_id = models.AutoField(primary_key=True)
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
