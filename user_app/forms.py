from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    name = 10
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder' : 'Повтори пароль', 'class': 'confirm'}),
    )
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email' : forms.EmailInput(attrs={'placeholder' : 'you@example.com'}),
            'password' : forms.PasswordInput(attrs={'placeholder' : 'Введи пароль'})
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('User with this email already exists.')
        return email
    def clean(self):
        
        clean_data = super().clean()
        password = clean_data.get('password') 
        confirm_password = clean_data.get('confirm_password')
        if password != confirm_password:
            self.add_error("password", "Password did'nt match")
            self.add_error("confirm_password", "Password did'nt match")
        return clean_data