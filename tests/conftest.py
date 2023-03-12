from django.conf import settings


def pytest_configure():
    settings.configure(INSTALLED_APPS=["django_mermaid.apps.MermaidConfig"])
