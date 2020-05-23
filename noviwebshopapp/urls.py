from django.urls import path
from django.contrib.auth import views as auth_views
from noviwebshopapp import views

app_name = 'noviwebshopapp'

urlpatterns = [
    path('',
        views.index_view.IndexListView.as_view(),
        name='index'),
    path('painting/<int:pk>/',
        views.painting_detail_view.PaintingDetailView.as_view(),
        name='painting_detail'),
    path('painting/create/',
        views.upload_painting_view.UploadPaintingView.as_view(),
        name='create_painting'),
    path('painting/update/<int:pk>/',
        views.update_painting_view.UpdatePaintingView.as_view(),
        name='update_painting'),
    path('painting/delete/<int:pk>/',
        views.delete_painting_view.DeletePaintingView.as_view(),
        name='delete_painting'),
    path('inloggen/',
        auth_views.LoginView.as_view(template_name='noviwebshopapp/login.html'),
        name='login'),
    path('uitloggen/',
        auth_views.LogoutView.as_view(),
        name='logout'),
    path('registreren/',
        views.register_view.SignUp.as_view(),
        name='signup'),
    path('mypaintings',
        views.user_paintings_list.UserPaintingsListView.as_view(),
        name='user_paintings_list'),
]
