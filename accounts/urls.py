from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import CustomLoginView, CustomRegisterView

app_name = "accounts"


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", CustomRegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),

]
