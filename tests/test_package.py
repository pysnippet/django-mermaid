from django.test import override_settings
from unittest.mock import patch
from django.apps import apps

@override_settings(MERMAID_USE_CDN=False)
@patch('django_mermaid.apps.download_if_necessary')
def test_download_called_when_use_cdn_false(mock_download):
    # Re-run the AppConfig.ready() method manually
    app_config = apps.get_app_config('django_mermaid')
    app_config.ready()

    mock_download.assert_called_once()


@override_settings(MERMAID_USE_CDN=True)
@patch('django_mermaid.apps.download_if_necessary')
def test_download_not_called_when_use_cdn_true(mock_download):
    app_config = apps.get_app_config('django_mermaid')
    app_config.ready()

    mock_download.assert_not_called()