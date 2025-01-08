from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import PermissionDenied
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView, DetailView, UpdateView

from football_schedule.accounts.forms import AppUserCreationForm, AppUserLoginForm, EditProfileForm, \
    CustomPasswordResetForm
from football_schedule.accounts.models import AppUser, Profile
from football_schedule.common.mixins import DeleteCloudinaryFormValidMixin


# Create your views here.

class UserRegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = AppUserCreationForm
    success_url = reverse_lazy('home')


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = AppUserLoginForm
    success_url = reverse_lazy('create-schedule')


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('create-schedule')

        return super().dispatch(request, *args, **kwargs)


class UserChangePasswordView(PasswordChangeView):
    template_name = 'accounts/change-password.html'
    success_url = reverse_lazy('details')


class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/reset-password.html'  # The template for the password reset form
    email_template_name = 'accounts/password_reset_email.html'  # Email template to send password reset link
    subject_template_name = 'accounts/password_reset_subject.txt'  # Subject template for email
    success_url = reverse_lazy('password_reset_done')  # Redirect to 'done' page after successfully sending reset email
    form_class = CustomPasswordResetForm

class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/reset-password-done.html'  # The template to show the message about email being sent

# Password Reset Confirm View (for setting new password)
class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/reset-password-confirm.html'  # Template for new password form
    success_url = reverse_lazy('password_reset_complete')  # Redirect after successful password reset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile'] = Profile.objects.filter(user_id=self.request.user.id)

        return context

# Password Reset Complete View (after password is successfully reset)
class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/reset-password-complete.html'  # Template to show reset


class UserDetailsView(DetailView):
    template_name = 'accounts/account-details.html'
    model = AppUser

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.request.user.id != self.object.pk:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class UserEditView(DeleteCloudinaryFormValidMixin,UpdateView):
    template_name = 'accounts/account-edit.html'
    form_class = EditProfileForm
    model = Profile
    cloudinary_delete_fields = ('profile_picture','club_emblem')

    def get_success_url(self):
        return reverse_lazy(
            'details',
            kwargs={
                'pk': self.object.pk
            }
        )

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.request.user.id != self.object.user_id:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['appuser'] = self.request.user

        return context


