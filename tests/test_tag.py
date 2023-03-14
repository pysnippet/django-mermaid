from os.path import dirname
from os.path import exists
from os.path import join

from django.conf import settings
from django.template import Context
from django.template import Template
from django.test import override_settings

from django_mermaid.templatetags import DEFAULT_THEME


def test_tag_use_in_template(version):
    theme = getattr(settings, "MERMAID_THEME", DEFAULT_THEME)
    template = Template("{% load mermaid %}{% mermaid content %}")
    template = template.render(Context({"content": "graph LR; A-->B;"}))
    assert template == (
            "<div class=\"mermaid\">graph LR; A-->B;</div><script src=\"mermaid/%s/mermaid.js\"></script>"
            "<script>mermaid.initialize({\"startOnLoad\": true, theme: \"%s\"});</script>" % (version, theme)
    )


@override_settings(MERMAID_THEME="forest")
def test_tag_use_settings_theme(version):
    template = Template("{% load mermaid %}{% mermaid content %}")
    template = template.render(Context({"content": "graph LR; A-->B;"}))
    assert template == (
            "<div class=\"mermaid\">graph LR; A-->B;</div><script src=\"mermaid/%s/mermaid.js\"></script>"
            "<script>mermaid.initialize({\"startOnLoad\": true, theme: \"forest\"});</script>" % version
    )


def test_tag_use_custom_theme(version):
    template = Template("{% load mermaid %}{% mermaid content \"dark\" %}")
    template = template.render(Context({"content": "graph LR; A-->B;"}))
    assert template == (
            "<div class=\"mermaid\">graph LR; A-->B;</div><script src=\"mermaid/%s/mermaid.js\"></script>"
            "<script>mermaid.initialize({\"startOnLoad\": true, theme: \"dark\"});</script>" % version
    )


def test_tag_use_custom_version(version):
    static_dir = join(dirname(__file__), "..", "src", "django_mermaid", "static")
    assert exists(join(static_dir, "mermaid", version, "mermaid.js"))
