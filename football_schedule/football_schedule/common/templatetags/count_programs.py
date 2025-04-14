from django import template
from football_schedule.programs.models import DisplayProgramData

register = template.Library()

@register.simple_tag
def count_programs():
    last_program = DisplayProgramData.objects.last()
    return last_program.id if last_program else None
