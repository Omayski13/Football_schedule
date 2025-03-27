from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

# Create your models here.

class Match(models.Model):
    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='matches',
    )

    team_1 = models.CharField(
        max_length=50
    )

    team_1_emblem = CloudinaryField(
        'club_emblem',
        folder='programs',
        null=True,
        blank=True,
    )

    team_2 = models.CharField(
        max_length=50
    )
    team_2_emblem = CloudinaryField(
        'club_emblem',
        folder='programs',
        null=True,
        blank=True,
    )

    date = models.DateField()

    time = models.TimeField()

    place = models.CharField(
        max_length=100,
    )


class DisplayProgramData(models.Model):
    user=models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='display_program'
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



