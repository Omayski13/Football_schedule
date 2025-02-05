from django.db import models


class TypeChoices(models.TextChoices):
    TRAINING = 'Тренировка', 'Тренировка'
    MACH = 'Мач', 'Мач'


class MonthChoices(models.TextChoices):
    JANUARY = 'Януари', 'Януари'
    FEBRUARY = 'Февруари', 'Февруари'
    MARCH = 'Март', 'Март'
    APRIL = 'Април', 'Април'
    MAY = 'Май', 'Май'
    JUNE = 'Юни', 'Юни'
    JULY = 'Юли', 'Юли'
    AUGUST = 'Август', 'Август'
    SEPTEMBER = 'Септември', 'Септември'
    OCTOBER = 'Октомври', 'Октомври'
    NOVEMBER = 'Ноември', 'Ноември'
    DECEMBER = 'Декември', 'Декември'


class ColorChoices(models.TextChoices):
    BLUE = 'blue', 'син'
    YELLOW = 'yellow', 'жълт'
    RED = 'red', 'червен'
    GREEN = 'green', 'зелен'
