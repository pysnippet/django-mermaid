from distutils import dir_util
from os.path import dirname, join, exists
from urllib.request import urlretrieve

from django.apps import AppConfig


class MermaidConfig(AppConfig):
    name = "django_mermaid"

    def ready(self):
        """Download mermaid.js from CDN if not already present"""
        cdn = "https://cdnjs.cloudflare.com/ajax/libs/mermaid/9.4.3/mermaid.js"
        static = join(dirname(__file__), "static")
        if not exists(join(static, "mermaid.js")):
            dir_util.create_tree(static, ["mermaid.js"])
            urlretrieve(cdn, join(static, "mermaid.js"))
