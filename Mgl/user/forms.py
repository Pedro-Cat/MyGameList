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

    nick = forms.CharField(
        max_length=20, 
        widget=forms.widgets.Textarea(
            attrs={
                'name': 'nick',
                'maxLength': '20',
                'rows': '1',
            }
        )
    )

    class Meta:
        model = Profile
        fields = ['nick', 'avatar', 'birth_date']
        widgets = {
            # Customizing the 'birth_date' input
            'birth_date': forms.DateInput(attrs={'type' : 'date'})

        }

