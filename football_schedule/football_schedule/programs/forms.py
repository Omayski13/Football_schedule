from django import forms

from football_schedule.programs.models import Match


class MatchBaseForm(forms.ModelForm):
    class Meta:
        model = Match
        exclude = ('author',)
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
        labels = {
            'team_1': 'Отбор',
            'team_1_emblem': 'Отбор Емблема',
            'team_2': 'Противник',
            'team_2_emblem': 'Противник Емблема',
            'date': 'Дата',
            'time': 'Час',
            'place': 'Място',

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'wide-input-small'
            })

class MatchCreateForm(MatchBaseForm):
    pass


class MatchEditForm(MatchBaseForm):
    pass








