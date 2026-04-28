from .views import RegisterPageView, RegisterView, LoginView, RegisterFormView, LoginFormView, ConfirmEmailFormView
from django.urls import path
urlpatterns = [
    path('auth-form/', RegisterPageView.as_view(), name='auth-form'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('form/register/', RegisterFormView.as_view(), name='form-register'),
    path('form/login/', LoginFormView.as_view(), name='form-login'),
    path('form/confirm-email/', ConfirmEmailFormView.as_view(), name='form-confirm-email'),
]