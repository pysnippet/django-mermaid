import pathlib
from urllib.request import urlretrieve

from django.apps import AppConfig
from django.conf import settings

from .templatetags import DEFAULT_VERSION


class MermaidConfig(AppConfig):
    name = "django_mermaid"

    def ready(self):
        """Download mermaid.js from CDN if not already present"""
        version = getattr(settings, "MERMAID_VERSION", DEFAULT_VERSION)
        cdn = "https://cdnjs.cloudflare.com/ajax/libs/mermaid/%s/mermaid.min.js" % version
        current_dir = pathlib.Path(__file__).parent
        static_dir = current_dir / "static"
        mermaid_dir = static_dir / "mermaid" / version
        mermaid_js = mermaid_dir / "mermaid.js"
        if not mermaid_js.exists() or \
               mermaid_js.stat().st_size == 0:
            mermaid_dir.mkdir(parents=True, exist_ok=True)
            urlretrieve(cdn, str(mermaid_js))
