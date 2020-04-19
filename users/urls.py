from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("login", auth_views.LoginView.as_view(), name="users-login"),
    path("logout", views.logout_view, name="users-logout"),
    path("register", views.register, name="users-register"),

]
