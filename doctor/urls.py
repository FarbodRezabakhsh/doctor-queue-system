from django.urls import path
from .views import LoginDoctorView,DoctorHomeView,RegisterDoctorView,LogoutDoctorView,DoctorDetailView

app_name = "doctor"


urlpatterns = [
    path("", DoctorHomeView.as_view(), name="doctor_home"),
    path("doctor/register/", RegisterDoctorView.as_view(), name="doctor_register"),
    path("doctor/login/", LoginDoctorView.as_view(), name="doctor_login"),
    path("doctor/logout/", LogoutDoctorView.as_view(), name="doctor_logout"),
    path("doctor/<int:id>/",DoctorDetailView.as_view(), name="doctor_detail"),
]
