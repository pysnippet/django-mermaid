from os.path import dirname
from os.path import exists
from os.path import join

from django.template import Context
from django.template import Template

from django_mermaid.templatetags import MERMAID_VERSION
from django_mermaid.templatetags.mermaid import mermaid


def test_tag_renders():
    assert mermaid("graph LR; A-->B;") == (
            "<div class=\"mermaid\">graph LR; A-->B;</div><script src=\"mermaid/%s/mermaid.js\"></script>"
            "<script>mermaid.initialize({\"startOnLoad\": true, theme: \"default\"});</script>" % MERMAID_VERSION
    )


def test_tag_use_in_template():
    template = Template("{% load mermaid %}{% mermaid content %}")
    template = template.render(Context({"content": "graph LR; A-->B;"}))
    assert template == (
            "<div class=\"mermaid\">graph LR; A-->B;</div><script src=\"mermaid/%s/mermaid.js\"></script>"
            "<script>mermaid.initialize({\"startOnLoad\": true, theme: \"default\"});</script>" % MERMAID_VERSION
    )


def test_tag_use_in_template_with_arguments():
    template = Template("{% load mermaid %}{% mermaid content \"forest\" %}")
    template = template.render(Context({"content": "graph LR; A-->B;"}))
    assert template == (
            "<div class=\"mermaid\">graph LR; A-->B;</div><script src=\"mermaid/%s/mermaid.js\"></script>"
            "<script>mermaid.initialize({\"startOnLoad\": true, theme: \"forest\"});</script>" % MERMAID_VERSION
    )


def test_tag_use_custom_version():
    static_dir = join(dirname(__file__), "..", "src", "django_mermaid", "static")
    assert exists(join(static_dir, "mermaid", MERMAID_VERSION, "mermaid.js"))
