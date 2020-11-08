from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username="username", password="password")
        if user == None:
#            attempt = request.session.get("attempt") or 0
#            request.session['attempt'] = attempt + 1
            return redirect("/invalid-password")