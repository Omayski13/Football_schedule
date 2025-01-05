from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from football_schedule.accounts.models import Profile
from football_schedule.common.mixins import CloudinaryImageValidatorMixin

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

class EditProfileForm(CloudinaryImageValidatorMixin,forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

    def clean_club_emblem(self):
        return self.validate_field('club_emblem')

    def clean_profile_picture(self):
        return self.validate_field('profile_picture')