import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
@mark_safe
def mermaid(text=""):
    return markdown.markdown(text)
