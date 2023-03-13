from django.conf import settings

MERMAID_VERSION = getattr(
    settings,
    "MERMAID_VERSION",
    "9.4.3",  # default to latest stable version
)

__all__ = ["MERMAID_VERSION"]
