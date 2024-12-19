from django.contrib.auth import get_user_model
from django.db import models

from football_schedule.schedules.choices import TypeChoices

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
