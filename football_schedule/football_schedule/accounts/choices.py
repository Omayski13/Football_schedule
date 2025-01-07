from django.db import models


class AccountsLicenceChoices(models.TextChoices):
    UEFA_PRO = 'Uefa PRO', 'Uefa PRO'
    UEFA_A = 'Uefa A', 'Uefa A'
    UEFA_B = 'Uefa B', 'Uefa B'
    UEFA_C = 'Uefa C', 'Uefa C'
    NATIONAL_C = 'Национален C', 'Национален C'
    GRASSROOTS_D = 'Grassroots D', 'Grassroots D'
    NONE = 'Без лиценз', 'Без лиценз'
