from django.urls import path, re_path
from main import views

urlpatterns = [

    # The home page
    path('', views.HomeView, name='home'),
]