from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import View
from .signals import user_registered

from .forms import CustomUserCreationForm
from .models import CustomUser


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate the user until email confirmation
            user.save()
            user_registered.send(sender=CustomUser, user=user, request=request)  # Trigger the custom signal
            return render(request, 'registration/confirm_email.html')  # Tell the user to check their email
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('profile')  # یا هر صفحه‌ای که می‌خواهید پس از ورود نشان داده شود
    else:
        return render(request, 'registration/activation_invalid.html')  # صفحه‌ای که نشان می‌دهد لینک تأیید معتبر نیست


@login_required
def profile(request):
    return render(request, 'users/profile.html')


class LogoutConfirmView(View):
    template_name = 'registration/logout_confirm.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        auth_logout(request)
        return redirect('logged_out')


class LoggedOutView(View):
    template_name = 'registration/logged_out.html'

    def get(self, request):
        return render(request, self.template_name)


@login_required
def login_done(request):
    return render(request, 'registration/login_done.html')
