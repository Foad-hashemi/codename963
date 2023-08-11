from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import View, FormView
from django import forms

from django.forms.utils import ValidationError
from .forms import RegisterForm, LoginForm


class Register(FormView):
    template_name = 'Accounts/register.html'
    form_class = RegisterForm
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Login(FormView):
    template_name = "Accounts/register.html"
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user=user)
        return super().form_valid(form)


