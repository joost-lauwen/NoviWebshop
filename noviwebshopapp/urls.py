from django.urls import path
from noviwebshopapp import views

app_name = 'noviwebshopapp'

urlpatterns = [
    path('', views.index_view.IndexListView.as_view(), name='index'),
    path('painting/<int:pk>/', views.painting_detail_view.PaintingDetailView.as_view(), name='painting_detail'),
    path('painting/create/', views.upload_painting_view.UploadPaintingView.as_view(), name='create_painting'),
    path('painting/update/<int:pk>/', views.update_painting_view.UpdatePaintingView.as_view(), name='update_painting'),
    path('painting/delete/<int:pk>/', views.delete_painting_view.DeletePaintingView.as_view(), name='delete_painting'),

    # path('uploadpainting/', views.views.painting_form_view, name='painting_form_view'),
    # path('registreren/', views.views.registration, name="Registreren"),
    # path('inloggen/', views.views.user_login, name="Inloggen")
]
