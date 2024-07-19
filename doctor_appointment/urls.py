from django.contrib import admin
from django.urls import path, include

from users import views
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('doctors/', include('doctors.urls')),
    path('appointments/', include('appointments.urls')),
    path('feedback/', include('feedback.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('profile/', views.profile, name='profile'),

]
