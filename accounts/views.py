from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.contrib import messages
from django.db.utils import IntegrityError
from django.views.generic import CreateView, UpdateView, TemplateView, ListView, DetailView
from django.views.generic import FormView
from django.core.exceptions import ValidationError

from .forms import UserLoginForm, CustomUserForm, ChargeFormClass
from accounts.models import User, Profile, Wallet


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
        value = self.request.POST.get('phone_number')
        user_email = self.request.POST.get('email')
        user = get_object_or_404(User, email=self.request.user)

        if User.objects.exclude(id=user.id).filter(email=user_email).exists() or User.objects.exclude(
                id=user.id).filter(phone_number=value).exists():
            messages.error(self.request, 'Email or phone number already exists. Please use a different email address.',
                           'error')
            return redirect(reverse('accounts:profile', kwargs={'pk': self.request.user.id}))

        try:
            user.phone_number = value
            user.email = user_email
            user.save()
        except Exception as e:
            messages.error(self.request, f'An error occurred: {e}', 'error')
            return redirect(reverse('accounts:profile', kwargs={'pk': self.request.user.id}))

        return super(ProfileEditView, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_email = User.objects.get(email=self.request.user)
        context['username'] = user_email
        return context


class ChargeWalletView(LoginRequiredMixin, FormView):
    template_name = 'accounts/charge_wallet.html'
    form_class = ChargeFormClass
    success_url = '/accounts/success_wallet/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        user = Wallet.objects.get(user=self.request.user)
        new_balance = user.balance + form.cleaned_data['balance']
        user.balance = new_balance
        user.save()
        return super().form_valid(form)


class ShowWalletView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/show_wallet.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        user_wallet = Wallet.objects.get(user=user)
        context["balance"] = user_wallet.balance
        return context


class SuccessChargeView(LoginRequiredMixin, View):
    template_name = 'accounts/success_charge.html'

    def get(self, request):
        user_wallet = Wallet.objects.get(user=request.user)
        return render(request, self.template_name, context={'balance': user_wallet.balance})

