from os.path import exists, join
from unittest.mock import patch

from django.apps import apps
from django.test import override_settings

try:
    import site

    site_packages = site.getsitepackages()[0]
except (ImportError, IndexError):
    import sysconfig

    site_packages = sysconfig.get_paths()["purelib"]


@override_settings(MERMAID_USE_CDN=False)
@patch("django_mermaid.apps.download_if_necessary")
def test_download_called_when_use_cdn_false(mock_download):
    # Re-run the AppConfig.ready() method manually
    app_config = apps.get_app_config("django_mermaid")
    app_config.ready()

    mock_download.assert_called_once()


@override_settings(MERMAID_USE_CDN=True)
@patch("django_mermaid.apps.download_if_necessary")
def test_download_not_called_when_use_cdn_true(mock_download):
    app_config = apps.get_app_config("django_mermaid")
    app_config.ready()

    mock_download.assert_not_called()


def test_tag_use_custom_version():
    static_dir = join(site_packages, "django_mermaid", "static")
    assert exists(join(static_dir, "mermaid", "8.6.3", "mermaid.js"))
    assert exists(join(static_dir, "mermaid", "9.4.3", "mermaid.js"))
