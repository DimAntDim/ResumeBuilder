from account_auth.forms import LogInForm, RegisterForm
from django.contrib.auth import login, logout, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



UserModel = get_user_model()


def user_registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user home page')
    form = LogInForm()
    context = {
        'form': form,
    }
    return render(request, 'account/login.html', context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')
