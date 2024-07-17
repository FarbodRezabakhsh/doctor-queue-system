from django.test import TestCase, Client
from django.urls import reverse
from doctors.models import Doctor
from appointments.models import Appointment
from feedback.models import Feedback
from django.contrib.auth.models import User
from users.models import CustomUser
from doctors.forms import SearchForm

class DoctorDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.doctor = Doctor.objects.create(name="Dr. Smith", specialization="Cardiologist",
                                            location="Private Clinic", fee=100, day_of_week="Monday",
                                            start_time="09:00", end_time="16:00")

        self.doctor2 = Doctor.objects.create(name="Dr. Jones", specialization="Dermatologist",
                                             location="Alzahra Hospital", fee=200, day_of_week="Tuesday",
                                             start_time="10:00", end_time="17:00")


    def test_doctor_detail_view(self):
        response = self.client.get(reverse('doctor_detail', args=[self.doctor.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors/doctor_detail.html')
        self.assertContains(response, self.doctor.name)

    def test_doctor_list_view_status_code(self):
        response = self.client.get(reverse('doctor_list'))
        self.assertEqual(response.status_code, 200)

    def test_doctor_list_view_template(self):
        response = self.client.get(reverse('doctor_list'))
        self.assertTemplateUsed(response, 'doctors/doctor_list.html')

    def test_doctor_list_view_search(self):
        response = self.client.get(reverse('doctor_list'), {'query': 'Smith'})
        self.assertContains(response, "Dr. Smith")
        self.assertContains(response, "Dr. Jones")

    def test_doctor_list_view_no_query(self):
        response = self.client.get(reverse('doctor_list'))
        self.assertContains(response, "Dr. Smith")
        self.assertContains(response, "Dr. Jones")
