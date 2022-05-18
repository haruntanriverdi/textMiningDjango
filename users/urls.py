from . import views

from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view, name="login"),
    #path('register/', views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"),
]