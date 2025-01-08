from django import template
from football_schedule.schedules.models import DisplayScheduleData

register = template.Library()

@register.simple_tag
def count_schedules():
    last_schedule = DisplayScheduleData.objects.last()
    return last_schedule.id if last_schedule else None
