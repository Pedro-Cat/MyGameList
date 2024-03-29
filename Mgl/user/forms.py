from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile

# Formulário de criação de usuário
class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nick', 'avatar', 'birth_date']

# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
