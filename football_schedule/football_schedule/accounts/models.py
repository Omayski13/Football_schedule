from cloudinary.models import CloudinaryField
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from football_schedule.accounts.choices import AccountsLicenceChoices, TeamGenerationChoices
from football_schedule.accounts.managers import AppUserManager


# Create your models here.

class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": _("Потребител с този имейл вече е регистриран"),
        }
    )

    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='appuser_set',
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=_('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='appuser_set',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AppUserManager()

class Profile(models.Model):
    user = models.OneToOneField(
        to=AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='profile',
    )

    first_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    club = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    club_emblem = CloudinaryField(
        'club_emblem',
        folder='accounts',
        null=True,
        blank=True,
    )

    team_generation_choice = models.CharField(
        max_length=20,
        choices=TeamGenerationChoices.choices,
        blank=False,
        null=False,
    )

    team_generation = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    profile_picture = CloudinaryField(
        'image',
        folder='accounts',
        null=True,
        blank=True,
    )

    license = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        choices=AccountsLicenceChoices.choices
    )

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return f'{self.user}'

    @property
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        if self.first_name and not self.last_name:
            return self.first_name
        if self.last_name and not self.first_name:
            return self.last_name
        return None
