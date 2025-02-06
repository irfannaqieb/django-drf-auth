from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(field, css_class):
    if field.errors:
        css_class += ' border-red-500'
    return field.as_widget(attrs={
        "class": css_class,
        "placeholder": field.label
    }) 