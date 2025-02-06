from django.urls import path
from . import views

urlpatterns = [
    path("token_login/", views.token_login, name="token_login"),
    path("token_register/", views.token_register, name="token_register"),
    path("session_login/", views.session_login, name="session_login"),
    path("session_register/", views.session_register, name="session_register"),
]
