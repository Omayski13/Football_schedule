from cloudinary.models import CloudinaryField
from django import forms
from django.forms import formset_factory, DateInput, TimeInput

from football_schedule.common.mixins import CloudinaryImageValidatorMixin
from football_schedule.schedules.choices import MonthChoices
from football_schedule.schedules.models import Week, DisplayScheduleData


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'wide-input-small'
            })

class WeekEditForm(WeekForm):
    pass


class DisplayForm(CloudinaryImageValidatorMixin,forms.ModelForm):
    class Meta:
        model = DisplayScheduleData
        exclude = ('user',)

    def clean_club_emblem(self):
        return self.validate_field('club_emblem')

    def clean_coach_photo(self):
        return self.validate_field('coach_photo')

    def clean(self):
        cleaned_data = super().clean()

        # Handle club_emblem
        if not self.cleaned_data.get('club_emblem') and self.initial.get('club_emblem'):
            cleaned_data['club_emblem'] = self.initial['club_emblem']

        # Handle coach_photo
        if not self.cleaned_data.get('coach_photo') and self.initial.get('coach_photo'):
            cleaned_data['coach_photo'] = self.initial['coach_photo']

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'wide-input'
            })


