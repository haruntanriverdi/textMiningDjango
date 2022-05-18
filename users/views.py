from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import LoginForm

from textMiningDjango.decorators import unauthenticated_user

@unauthenticated_user
def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)


            if user is not None:

                login(request, user)
                messages.add_message(request, messages.SUCCESS, f'Welcome {user.username}')
                return redirect("/")

            else:
                messages.add_message(request, messages.ERROR, 'Invalid input...')
                return render(request, 'login.html', {"form": form}, status=401)

        else:
            messages.add_message(request, messages.ERROR, 'Invalid form...')

    return render(request, "login.html", {"form": form,})


def logout_user(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS,
                         'Login successfully')

    return redirect(reverse('login'))