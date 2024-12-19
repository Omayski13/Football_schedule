from django import template
from datetime import timedelta, date, datetime

register = template.Library()

@register.filter
def add_days(value, days):
    if isinstance(value, (date, datetime)):
        return value + timedelta(days=days)
    return value
