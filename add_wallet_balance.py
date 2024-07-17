import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctor_appointment.settings')
django.setup()

from django.contrib.auth import get_user_model
from doctors.models import Doctor
# دریافت مدل کاربر سفارشی
User = get_user_model()

# یافتن کاربر با ایمیل مشخص
user = User.objects.get(email="shabanimehran@gmail.com")
doctor =Doctor.objects.get(name='Bruce Madden')
# افزودن مقدار 1000 به موجودی کیف پول
user.wallet_balance += 500
doctor.email = user.email
# ذخیره تغییرات در پایگاه داده
user.save()
doctor.save()
print(f"موجودی جدید کیف پول کاربر: {user.wallet_balance}")
print (f'email created for {doctor.name}, and is :{doctor.email}')