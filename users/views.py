from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as auth_logout
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


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
