from django import template

register = template.Library()

@register.filter('upper_function')
def upper_function(value):
    return value.upper()

@register.filter('birthday_date')
def birthday_date(value,format_string="%d-%m-%Y"):
    return value.strftime(format_string)