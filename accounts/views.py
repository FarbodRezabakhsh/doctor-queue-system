from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import UserLoginForm, CustomUserForm
from accounts.models import User, Profile
# Create your views here.


class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    fields = "email", "password"
    form_class = UserLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("doctor:home")


class CustomRegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = CustomUserForm

    def get_success_url(self):
        print('hi')
        return reverse_lazy('accounts:login')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("doctor:home")
            # Redirect to the task list page if user is already authenticated
        return super(CustomRegisterView, self).get(*args, **kwargs)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/profile.html'
    model = Profile
    fields = ['name', 'age', 'gender']
    success_url = reverse_lazy("doctor:home")

    def form_valid(self, form):
        value = self.request.POST['phone_number']
        user_email = self.request.POST['email']
        user = get_object_or_404(User, email=self.request.user)
        user.phone_number = value
        user.email = user_email
        user.save()
        return super(ProfileEditView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_email = User.objects.get(email=self.request.user)
        context['username'] = user_email
        return context
