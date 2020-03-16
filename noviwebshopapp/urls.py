from django.urls import path
from noviwebshopapp import views

urlpatterns = [
    path('', views.index, name='index')
]
