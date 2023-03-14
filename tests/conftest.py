import pytest
from django.conf import settings

from django_mermaid.templatetags import DEFAULT_VERSION


def pytest_configure():
    settings.configure(
        INSTALLED_APPS=[
            "django_mermaid.apps.MermaidConfig"
        ],
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
            },
        ],
        MERMAID_VERSION="8.6.3",  # Use a specific version of mermaid
    )


@pytest.fixture
def version():
    return getattr(settings, "MERMAID_VERSION", DEFAULT_VERSION)
