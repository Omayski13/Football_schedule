from django import forms
from django.forms import formset_factory, DateInput, TimeInput

from football_schedule.schedules.models import Week


class WeekForm(forms.ModelForm):
    class Meta:
        model = Week
        exclude = ('author',)

    start_date = forms.DateField(
        widget=DateInput(attrs={'type': 'date'})  # Using HTML5 date input
    )

    monday_time = forms.TimeField(
        widget=TimeInput(attrs={'type': 'time',}),
        required=False,# Using HTML5 time input
    )
    tuesday_time = forms.TimeField(
        widget=TimeInput(attrs={'type': 'time'}),
        required=False,
    )
    wednesday_time = forms.TimeField(
        widget=TimeInput(attrs={'type': 'time'}),
        required=False,
    )
    thursday_time = forms.TimeField(
        widget=TimeInput(attrs={'type': 'time'}),
        required=False,
    )
    friday_time = forms.TimeField(
        widget=TimeInput(attrs={'type': 'time'}),
        required=False,
    )
    saturday_time = forms.TimeField(
        widget=TimeInput(attrs={'type': 'time'}),
        required=False,
    )
    sunday_time = forms.TimeField(
        widget=TimeInput(attrs={'type': 'time'}),
        required=False,
    )