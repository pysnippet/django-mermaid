# Django Mermaid

Django template tag for showing mermaid diagrams.

[![PyPI](https://img.shields.io/pypi/v/django-mermaid.svg)](https://pypi.org/project/django-mermaid/)
[![License](https://img.shields.io/pypi/l/django-mermaid.svg)](https://github.com/ArtyomVancyan/django-mermaid/blob/master/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![Tests](https://github.com/ArtyomVancyan/django-mermaid/actions/workflows/tests.yml/badge.svg)](https://github.com/ArtyomVancyan/django-mermaid/actions/workflows/tests.yml)

## Install

```shell
python -m pip install django-mermaid
```

## Configuration

Add the `django_mermaid.apps.MermaidConfig` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    ...,  # other apps
    'django_mermaid.apps.MermaidConfig',
]
```

## Usage

Once you have installed the app, you can use the `mermaid` template tag in your templates.

```html
{% load mermaid %}

{% mermaid "graph LR; A-->B;" %}
```

## Contribute

Any contribution is welcome. If you have any ideas or suggestions, feel free to open an issue or a pull request. And
don't forget to add tests for your changes.

## License

Copyright (C) 2023 Artyom Vancyan. [MIT](https://github.com/ArtyomVancyan/django-mermaid/blob/master/LICENSE)
