from os.path import dirname
from os.path import exists
from os.path import join

from django.template import Context
from django.template import Template

from django_mermaid.templatetags.mermaid import mermaid


def test_tag_renders():
    assert mermaid("graph LR; A-->B;") == (
        """<div class="mermaid">graph LR; A-->B;</div><script src="mermaid.js"></script>"""
        """<script>mermaid.initialize({"startOnLoad": true, theme: "default"});</script>"""
    )


def test_tag_use_in_template():
    template = Template("{% load mermaid %}{% mermaid content %}")
    template = template.render(Context({"content": "graph LR; A-->B;"}))
    assert template == (
        """<div class="mermaid">graph LR; A-->B;</div><script src="mermaid.js"></script>"""
        """<script>mermaid.initialize({"startOnLoad": true, theme: "default"});</script>"""
    )


def test_tag_use_in_template_with_arguments():
    template = Template("{% load mermaid %}{% mermaid content \"forest\" %}")
    template = template.render(Context({"content": "graph LR; A-->B;"}))
    assert template == (
        """<div class="mermaid">graph LR; A-->B;</div><script src="mermaid.js"></script>"""
        """<script>mermaid.initialize({"startOnLoad": true, theme: "forest"});</script>"""
    )


def test_tag_use_custom_version():
    assert exists(join(dirname(__file__), "..", "src", "django_mermaid", "static", "mermaid", "8.6.3", "mermaid.js"))
