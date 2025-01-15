from cloudinary.models import CloudinaryField
from django import forms
from django.forms import formset_factory, DateInput, TimeInput

from football_schedule.accounts.choices import TeamGenerationChoices
from football_schedule.common.mixins import CloudinaryImageValidatorMixin
from football_schedule.schedules.choices import MonthChoices
from football_schedule.schedules.models import Week, DisplayScheduleData


class WeekForm(forms.ModelForm):
    class Meta:
        model = Week
        exclude = ('author',)

    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'id': 'start_date',
                'type': 'date',  # HTML5 date input
                'data-week-start': '1' , # Week starts on Monday (if using a library like Bootstrap Datepicker)
            }
        )
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

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'wide-input-small'
            })

            if '_type' in field_name:
                field.label = 'Вид'
            elif '_time' in field_name:
                field.label = 'Час'
            elif '_place' in field_name:
                field.label = 'Място'
            elif 'start' in field_name:
                field.label = 'Начална дата'

            if field.required:
                field.label = f'{field.label}*'



class WeekEditForm(WeekForm):
    pass


class DisplayForm(CloudinaryImageValidatorMixin, forms.ModelForm):
    class Meta:
        model = DisplayScheduleData
        exclude = ('user',)
        widgets = {
            'team_generation_choice': forms.RadioSelect,
        }
        labels = {
            'club_emblem': 'Клубна Емблема',
            'club': 'Клуб',
            'team_generation_choice': 'Отбор/Набор',
            'team_generation': 'Отбор/Набор',
            'coach': 'Треньор',
            'coach_photo': 'Снимка на треньор',
            'month': 'Месец',
        }

    def clean_club_emblem(self):
        # Validate only if the field has a value
        club_emblem = self.cleaned_data.get('club_emblem')
        if not club_emblem:
            return None
        return self.validate_field('club_emblem')


    def clean_coach_photo(self):
        # Validate only if the field has a value
        coach_photo = self.cleaned_data.get('coach_photo')
        if not coach_photo:
            return None
        return self.validate_field('coach_photo')


    def clean(self):
        cleaned_data = super().clean()
        #Retain initial values if present and the field is left blank
        if not cleaned_data.get('club_emblem') and self.initial.get('club_emblem'):
            cleaned_data['club_emblem'] = self.initial['club_emblem']
        if not cleaned_data.get('coach_photo') and self.initial.get('coach_photo'):
            cleaned_data['coach_photo'] = self.initial['coach_photo']

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'wide-input'
            })

        # Explicitly set optional fields as not required
        self.fields['coach_photo'].required = False
        self.fields['club_emblem'].required = False

        self.fields['coach'].widget.attrs.update({
            'placeholder': 'Въведете име на треньор...'
        })

        self.fields['team_generation_choice'].required = True
        self.fields['team_generation_choice'].empty_label = None
        self.fields['team_generation_choice'].choices = TeamGenerationChoices

        self.fields['team_generation'].widget.attrs.update({
            'placeholder': 'Въведете набор/отбор...'
        })

        self.fields['club'].widget.attrs.update({
            'placeholder': 'Въведете име на клуб...'
        })

        self.fields['team_generation_choice'].widget.attrs.update({
            'class': ''
        })


