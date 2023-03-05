from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import Account

# Here we are created class for auth and register users

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Важно, ведите правильный email')

    class Meta: 
        model = Account
        fields = ["email", "username", "password1", "password2"]
