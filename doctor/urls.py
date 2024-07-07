from django.urls import path
from doctor.views import HomeView

app_name = "doctor"


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
