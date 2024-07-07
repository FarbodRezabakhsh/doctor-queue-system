from django.contrib import admin
from django.urls import path, include
from .views import home  # اضافه کردن این خط

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # اضافه کردن این خط
    path('doctors/', include('doctors.urls')),
    path('appointments/', include('appointments.urls')),
    path('feedback/', include('feedback.urls')),
    path('users/', include('users.urls')),
]
