from django import template
register = template.Library()

@register.simple_tag()
def multiply(qty, unit_price, *args, **kwargs):
    # you would need to do any localization of the result here
        
    return '{0:,}'.format(qty * unit_price)


@register.simple_tag()
def divide(value, arg):
    try:
        divi = int(value) / int(arg)
        return f'{divi:,.1f}'
    except (ValueError, ZeroDivisionError):
        return None