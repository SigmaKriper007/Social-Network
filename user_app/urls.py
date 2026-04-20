from django.urls import path
from .views import RegisterPageView, RegisterView

urlpatterns = [
    path('auth-form/', RegisterPageView.as_view(), name='auth-form'),
    path('register/', RegisterView.as_view(), name='register'),
]