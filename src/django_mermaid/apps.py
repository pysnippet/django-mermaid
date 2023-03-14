from distutils import dir_util
from os import stat
from os.path import dirname
from os.path import exists
from os.path import join
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
        static_dir = join(dirname(__file__), "static")
        mermaid_dir = join(static_dir, "mermaid", version)
        if not exists(join(mermaid_dir, "mermaid.js")) or \
                stat(join(mermaid_dir, "mermaid.js")).st_size == 0:
            dir_util.create_tree(mermaid_dir, ["mermaid.js"])
            urlretrieve(cdn, join(mermaid_dir, "mermaid.js"))
