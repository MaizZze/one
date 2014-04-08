__author__ = 'golikov'

from django import template

register = template.Library()

# @register.simple_tag
# def smart_column(groups):
#     return '<div class="col-xs-{val}>"'


@register.filter
def div(value, arg):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        value = int(value)
        arg = int(arg)
        if arg:
            return value / arg
    except:
        pass
    return ''
