import json

from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.safestring import mark_safe

from . import DEFAULT_THEME
from . import DEFAULT_VERSION

register = template.Library()


@register.simple_tag
@mark_safe
def mermaid(diagram=None, theme=None):
    """Render a mermaid diagram.

    :param diagram: The mermaid diagram definition
    :param theme: The mermaid theme to use (default, forest, dark, neutral, base). See https://mermaid.js.org/config/theming.
    """

    version = getattr(settings, "MERMAID_VERSION", DEFAULT_VERSION)
    theme = theme or getattr(settings, "MERMAID_THEME", DEFAULT_THEME)
    theme_variables = getattr(settings, "MERMAID_THEME_VARIABLES", {}) if theme == "base" else {}

    mermaid_uri = static("mermaid/%s/mermaid.js" % version)
    html = "<div class=\"mermaid\">%s</div><script src=\"%s\"></script>" % (diagram or "", mermaid_uri)
    init_properties = {"startOnLoad": True, "theme": theme, "themeVariables": theme_variables}
    return html + "<script>mermaid.initialize(%s);</script>" % json.dumps(init_properties)
