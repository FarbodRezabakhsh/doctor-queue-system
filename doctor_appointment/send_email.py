from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_test_email():
    mail_subject = 'Test Email'
    message = render_to_string('registration/acc_active_email.html', {
        'user': {'username': 'testuser'},
        'domain': 'example.com',
        'uid': 'uid',
        'token': 'token',
    })
    email = EmailMessage(mail_subject, message, to=['shabanimehran@gmail.com'])
    email.content_subtype = 'html'  # تنظیم نوع محتوای ایمیل به HTML
    email.send()

