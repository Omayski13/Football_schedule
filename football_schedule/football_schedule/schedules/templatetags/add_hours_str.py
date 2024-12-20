from django import template

register = template.Library()

@register.filter
def add_hours_str(value, string:str):
    if value is not None:
        return str(value) + str(string)
    return value