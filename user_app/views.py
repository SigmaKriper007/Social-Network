from django.views.generic import TemplateView
from django.views import View
from django.http import HttpRequest, JsonResponse
from .forms import RegistrationForm
# Create your views here.
class RegisterPageView(TemplateView):
    template_name = 'user_app/auth.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register_form'] = RegistrationForm()
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