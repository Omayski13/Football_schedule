from django.db import models


class TypeChoices(models.TextChoices):
    TRAINING = 'training', 'Тренировка'
    MACH = 'mach', 'Мач'


class MonthChoices(models.TextChoices):
    JANUARY = 'January', 'Януари'
    FEBRUARY = 'February', 'Февруари'
    MARCH = 'March', 'Март'
    APRIL = 'April', 'Април'
    MAY = 'May', 'Май'
    JUNE = 'June', 'Юни'
    JULY = 'July', 'Юли'
    AUGUST = 'August', 'Август'
    SEPTEMBER = 'September', 'Септември'
    OCTOBER = 'October', 'Октомври'
    NOVEMBER = 'November', 'Ноември'
    DECEMBER = 'December', 'Декември'