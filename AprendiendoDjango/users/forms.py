"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    """Sign up form."""

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(attrs={
            'id': 'inputEmail',
            'class': 'form-control',
            'placeholder': 'Correo electrónico'
        })
    )
    username = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.TextInput(attrs={
            'id': 'inputUsername',
            'class': 'form-control',
            'placeholder': 'Nome de usuario',
        }),
    )
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(attrs={
            'id': 'inputPassword',
            'class': 'form-control',
            'placeholder': 'Contrasinal',
            'auto-complete': 'new-password'
        })
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(attrs={
            'id': 'inputPasswordRepeat',
            'class': 'form-control',
            'placeholder': 'Repetir contrasinal'
        })
    )


    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Os contrasinais non coinciden.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()