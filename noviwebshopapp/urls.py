from django.urls import path
from noviwebshopapp import views

app_name = 'noviwebshopapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('uploadpainting/', views.painting_form_view, name='painting_form_view'),
    path('registreren/', views.users, name="Registreren")
]
