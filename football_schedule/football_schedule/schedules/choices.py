from django.db import models


class TypeChoices(models.TextChoices):
    TRAINING = 'training', 'Тренировка'
    MACH = 'mach', 'Мач'
