from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpRequest, JsonResponse
from .forms import RegistrationForm, LoginForm
# Create your views here.
class RegisterPageView(TemplateView):
    template_name = 'user_app/auth.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = RegistrationForm()
        context['login_form'] = LoginForm()
        return context

class RegisterView(View):
    def post(self, request: HttpRequest):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'User Created'
            })
        return JsonResponse({
            'error': form.errors.get_json_data()
        })

from django.urls import reverse

class LoginView(View):
    def post(self, request):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            login(request, login_form.user)

            return JsonResponse({
                "message": "Login Success",
                "redirect_url": reverse("home")
            })

        return JsonResponse({
            "error": login_form.errors.get_json_data()
        })
    
class RegisterFormView(View):
    def get(self, request):
        return render(request, 'user_app/particles/form_register.html', {
            'register_form': RegistrationForm()
        })


class LoginFormView(View):
    def get(self, request):
        return render(request, 'user_app/particles/form_login.html', {
            'login_form': LoginForm()
        })
    

class ConfirmEmailFormView(View):
    def get(self, request):
        return render(request, 'user_app/particles/form_confirm_email.html')