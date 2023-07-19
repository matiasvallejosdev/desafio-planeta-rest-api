from django import forms
from django.contrib.auth.forms import AuthenticationForm


# Customize login view
# https://stackoverflow.com/questions/62763849/how-to-customize-loginview

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username or email',
            }
        )
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password'
            }
        )
    )
