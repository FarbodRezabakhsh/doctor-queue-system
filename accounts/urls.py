from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import CustomLoginView, CustomRegisterView\
    ,ProfileEditView, ChargeWalletView, ShowWalletView, SuccessChargeView

app_name = "accounts"


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", CustomRegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path('profile/<int:pk>/', ProfileEditView.as_view(), name='profile'),
    path('show_wallet/<int:pk>/', ShowWalletView.as_view(), name='show_wallet'),
    path('charge_wallet/<int:pk>/', ChargeWalletView.as_view(), name='charge_wallet'),
    path('success_wallet/', SuccessChargeView.as_view(), name='success_wallet'),

]
