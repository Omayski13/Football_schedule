from datetime import timedelta

from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

from football_schedule.accounts.choices import TeamGenerationChoices
from football_schedule.schedules.choices import TypeChoices, MonthChoices, ColorChoices

UserModel = get_user_model()


# Create your models here.
class Week(models.Model):
    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='week'
    )

    start_date = models.DateField()

#MONDAY
    monday_type = models.CharField(
        choices=TypeChoices.choices,
        null=True,
        blank=True,
    )

    monday_time = models.TimeField(
        null=True,
        blank=True,
    )

    monday_place = models.CharField(
        null=True,
        blank=True,
    )

#TUESDAY
    tuesday_type = models.CharField(
        choices=TypeChoices.choices,
        null=True,
        blank=True,
    )

    tuesday_time = models.TimeField(
        null=True,
        blank=True,
    )

    tuesday_place = models.CharField(
        null=True,
        blank=True,
    )

#WEDNESDAY
    wednesday_type = models.CharField(
        choices=TypeChoices.choices,
        null=True,
        blank=True,
    )

    wednesday_time = models.TimeField(
        null=True,
        blank=True,
    )

    wednesday_place = models.CharField(
        null=True,
        blank=True,
    )

#THURSDAY
    thursday_type = models.CharField(
        choices=TypeChoices.choices,
        null=True,
        blank=True,
    )

    thursday_time = models.TimeField(
        null=True,
        blank=True,
    )

    thursday_place = models.CharField(
        null=True,
        blank=True,
    )

#FRIDAY
    friday_type = models.CharField(
        choices=TypeChoices.choices,
        null=True,
        blank=True,
    )

    friday_time = models.TimeField(
        null=True,
        blank=True,
    )

    friday_place = models.CharField(
        null=True,
        blank=True,
    )

#SUTURDAY
    saturday_type = models.CharField(
        choices=TypeChoices.choices,
        null=True,
        blank=True,
    )

    saturday_time = models.TimeField(
        null=True,
        blank=True,
    )

    saturday_place = models.CharField(
        null=True,
        blank=True,
    )

#SUNDAY
    sunday_type = models.CharField(
        choices=TypeChoices.choices,
        null=True,
        blank=True,
    )

    sunday_time = models.TimeField(
        null=True,
        blank=True,
    )

    sunday_place = models.CharField(
        null=True,
        blank=True,
    )

    def __str__(self):
        start_date = self.start_date.strftime("%d.%m.%Y")
        end_date = (self.start_date + timedelta(days=6)).strftime("%d.%m.%Y")
        return f"{start_date} - {end_date}"

class DisplayScheduleData(models.Model):
    user=models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='display_schedule'
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
    coach = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    coach_photo = CloudinaryField(
        'coach_photo',
        folder='accounts',
        null=True,
        blank=True,
    )
    month = models.CharField(
        choices=MonthChoices.choices,
        null=True,
        blank=True,
    )
    color = models.CharField(
        max_length=20,
        choices=ColorChoices.choices,
        default=ColorChoices.BLUE
    )

    def __str__(self):
        if self.month:
            return f"{self.club} - {self.team_generation} - {self.month}"
        else:
            return f"{self.club} - {self.team_generation}"
