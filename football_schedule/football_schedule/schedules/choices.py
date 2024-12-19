from django.db import models


class TypeChoices(models.TextChoices):
    TRAINING = 'Тренировка', 'Тренировка'
    MACH = 'Мач', 'Мач'
