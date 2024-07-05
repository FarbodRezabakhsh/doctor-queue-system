from django.urls import path

from user.views import CustomLoginView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="index"),

]
