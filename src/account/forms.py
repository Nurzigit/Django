from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account

# Here we are created class for auth and register users

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Важно, ведите правильный email')

    class Meta: 
        model = Account
        fields = ["email", "username", "password1", "password2"]

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput) #Widget нам нужен для того что б пароль не был виден

    class Meta:
       model = Account
       fields = ('email', 'password')

    # Здесь мы саздаем функ claen, кго работа заключается в том что он будет работать до того как подключиться сама форма
    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email = email, password = password):
            raise forms.ValidationError("Invalid email, or password")
        