from django import template
from django.templatetags.static import static
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
@mark_safe
def mermaid(diagram="", theme="default"):
    """Render a mermaid diagram.

    :param diagram: The mermaid diagram definition
    :param theme: The mermaid theme to use (default, forest, dark, neutral). See https://mermaid.js.org/config/theming.
    """

    html = "<div class=\"mermaid\">%s</div><script src=\"%s\"></script>" % (diagram, static("mermaid.js"))
    return html + "<script>mermaid.initialize({\"startOnLoad\": true, theme: \"%s\"});</script>" % theme
