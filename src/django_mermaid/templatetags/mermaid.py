import ast
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
    """Render a mermaid diagram, using a simple tag.

    {% mermaid "graph LR; A-->B;" "dark" %}

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


@register.tag(name="startmermaid")
def startmermaid(parser, token):
    """Render a mermaid diagram, using a block tag.

    {% startmermaid "dark" %}
        graph LR
            A-->B
    {% endmermaid %}

    This tag is identical to the {% mermaid %} simple tag but allows usage as a block.
    That can be useful for longer diagrams. Specifying the theme is optional.
    """

    bits = token.split_contents()
    if len(bits) > 1:
        theme = ast.literal_eval(bits[1])
    else:
        theme = None

    nodelist = parser.parse(('endmermaid',))
    parser.delete_first_token()

    return MermaidNode(nodelist, theme)


class MermaidNode(template.Node):
    def __init__(self, nodelist, theme):
        self.nodelist = nodelist
        self.theme = theme

    def render(self, context):
        diagram_content = self.nodelist.render(context)
        return mermaid(diagram=diagram_content, theme=self.theme)
