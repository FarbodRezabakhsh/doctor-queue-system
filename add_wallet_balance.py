import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctor_appointment.settings')
django.setup()

from django.contrib.auth import get_user_model

# دریافت مدل کاربر سفارشی
User = get_user_model()

# یافتن کاربر با ایمیل مشخص
user = User.objects.get(email="your_email.com")

# افزودن مقدار 1000 به موجودی کیف پول
user.wallet_balance += 50000

# ذخیره تغییرات در پایگاه داده
user.save()

print(f"موجودی جدید کیف پول کاربر: {user.wallet_balance}")
