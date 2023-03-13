from django.conf import settings


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
