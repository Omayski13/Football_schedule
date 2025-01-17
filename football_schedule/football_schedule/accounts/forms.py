from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.urls import reverse

from football_schedule.accounts.choices import TeamGenerationChoices
from football_schedule.accounts.models import Profile
from football_schedule.common.mixins import CloudinaryImageValidatorMixin

UserModel = get_user_model()

class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email',]
        error_messages = {
            'password_mismatch': 'Паролите не съвпадат.',  # Override the default error message
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        # Check if passwords match
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Паролите не съвпадат.', code='password_mismatch')

        return password2

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')

        if len(password1) < 8:
            self.add_error('password1', 'Паролата трябва да бъде поне 8 символа.')
        if password1.isdigit():
            self.add_error('password1', 'Паролата не може да бъде само цифри.')
        if not any(char.isdigit() for char in password1):
            self.add_error('password1', 'Паролата трябва да съдържа поне една цифра.')
        if not any(char.isupper() for char in password1):
            self.add_error('password1', 'Паролата трябва да съдържа поне една главна буква.')
        if not any(char.islower() for char in password1):
            self.add_error('password1', 'Паролата трябва да съдържа поне една малка буква.')
        if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password1):
            self.add_error('password1', 'Паролата трябва да съдържа поне един специален символ.')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['email'].widget.attrs.update({
            'placeholder': "Въведи валиден имейл...",
        })

        reset_password_url = reverse(
            'password-reset')  # Adjust 'password-reset' to your URL name for the password reset view.

        self.fields['email'].error_messages = {
            'required': 'Моля, въведете имейл адрес.',
            'invalid': 'Невалиден имейл адрес.',
            'unique': (
                'Потребител с този имейл вече е регистриран.<br>'
                f'<a href="{reset_password_url}">Забравена парола?</a>'
            ),
        }

        self.fields['password1'].required = True
        self.fields['password1'].help_text = "Паролата не може да бъда само цифри и трябва да бъде поне 8 символа"
        self.fields['password1'].widget.attrs.update({
            'placeholder': "Въведи парола...",
        })

        self.fields['password2'].required = True
        self.fields['password2'].help_text = ''
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Повтори парола...',
        })




class AppUserLoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Моля, въведете валиднен имейл и парола.',
        'inactive': 'Този акаунт е неактивен.',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder':'Въведете имейл...'
        })

        self.fields['password'].widget.attrs.update({
            'placeholder': 'Въведете парола...'
        })

class EditProfileForm(CloudinaryImageValidatorMixin,forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'team_generation_choice': forms.RadioSelect,
        }
        labels = {
            'first_name': 'Име',
            'last_name': 'Фамилия',
            'club': 'Клуб',
            'club_emblem': 'Клубна емблема',
            'team_generation_choice': 'Отбор/Набор',
            'team_generation': 'Отбор/Набор',
            'profile_picture': 'Профилна снимка',
            'license': 'Лиценз',
            'color': 'Графика цвят',
        }

    def clean_club_emblem(self):
        return self.validate_field('club_emblem')

    def clean_profile_picture(self):
        return self.validate_field('profile_picture')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'placeholder':'Въведете име...'
        })

        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Въведете фамилия...'
        })

        self.fields['club'].widget.attrs.update({
            'placeholder': 'Въведете име на клуб...'
        })

        self.fields['team_generation_choice'].required = True
        self.fields['team_generation_choice'].empty_label = None
        self.fields['team_generation_choice'].choices = TeamGenerationChoices
        self.fields['team_generation_choice'].widget.attrs.update({
            'class': ''
        })

        self.fields['team_generation'].widget.attrs.update({
            'placeholder': 'Въведете набор/отбор...'
        })


class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Check if the email exists in the database
        if not UserModel.objects.filter(email=email).exists():
            raise ValidationError("Няма регистриран потребител с този имейл.")

        return email