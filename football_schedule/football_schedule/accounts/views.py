from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from football_schedule.accounts.forms import AppUserCreationForm, AppUserLoginForm


# Create your views here.

class UserRegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = AppUserCreationForm
    success_url = reverse_lazy('schedule')


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = AppUserLoginForm
    success_url = reverse_lazy('schedule')


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('schedule')

        return super().dispatch(request, *args, **kwargs)

