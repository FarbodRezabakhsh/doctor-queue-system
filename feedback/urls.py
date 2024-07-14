from django.urls import path
from .views import give_feedback, feedback_confirm

urlpatterns = [
    path('give/<int:doctor_id>/', give_feedback, name='give_feedback'),
    path('confirm/<int:doctor_id>/', feedback_confirm, name='feedback_confirm'),
]
