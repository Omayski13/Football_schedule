from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from football_schedule.accounts.models import Profile

UserModel = get_user_model()

class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email',]


class AppUserLoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Моля, въведете валиднен имейл и парола.',
        'inactive': 'Този акаунт е неактивен.',
    }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)