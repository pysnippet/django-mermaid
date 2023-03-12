from django_mermaid.templatetags.mermaid import mermaid


def test_tag_renders():
    assert mermaid("graph LR; A-->B;") == (
        """<div class="mermaid">graph LR; A-->B;</div><script src="mermaid.js"></script>"""
        """<script>mermaid.initialize({"startOnLoad": true, theme: "default"});</script>"""
    )
