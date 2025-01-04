from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from football_schedule.accounts.forms import AppUserCreationForm, AppUserLoginForm, EditProfileForm
from football_schedule.accounts.models import AppUser, Profile


# Create your views here.

class UserRegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = AppUserCreationForm
    success_url = reverse_lazy('create-schedule')


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = AppUserLoginForm
    success_url = reverse_lazy('create-schedule')


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('create-schedule')

        return super().dispatch(request, *args, **kwargs)

class UserDetailsView(DetailView):
    template_name = 'accounts/account-details.html'
    model = AppUser

class UserEditView(UpdateView):
    template_name = 'accounts/account-edit.html'
    form_class = EditProfileForm
    model = Profile

    def get_success_url(self):
        return reverse_lazy(
            'details',
            kwargs={
                'pk': self.object.pk
            }
        )


