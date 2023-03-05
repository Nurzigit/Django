from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm


# Create logic func our forms and import new library

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save();
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_forms'] = form
    else: #Here GET request
        form = RegistrationForm();
        context['registration_forms'] = form
    return render(request, 'account/register.html', context)


# Logic for logout user
def logout_view(requset):
    logout(requset)
    return redirect('home')