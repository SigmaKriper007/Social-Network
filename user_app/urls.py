from django.urls import path
from .views import RegisterPageView, RegisterView, LoginView, RegisterFormView, LoginFormView

urlpatterns = [
    path('auth-form/', RegisterPageView.as_view(), name='auth-form'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('form/register/', RegisterFormView.as_view(), name='form-register'),
    path('form/login/', LoginFormView.as_view(), name='form-login'),
]