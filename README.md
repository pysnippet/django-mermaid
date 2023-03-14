# Django Mermaid

Django template tag for rendering mermaid diagrams.

[![PyPI](https://img.shields.io/pypi/v/django-mermaid.svg)](https://pypi.org/project/django-mermaid/)
[![License](https://img.shields.io/pypi/l/django-mermaid.svg)](https://github.com/ArtyomVancyan/django-mermaid/blob/master/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![Tests](https://github.com/ArtyomVancyan/django-mermaid/actions/workflows/tests.yml/badge.svg)](https://github.com/ArtyomVancyan/django-mermaid/actions/workflows/tests.yml)

## Install

```shell
python -m pip install django-mermaid
```

## Configuration

Add the `django_mermaid.apps.MermaidConfig` to your `INSTALLED_APPS` in your Django project's **settings.py** file.

```python
INSTALLED_APPS = [
    ...,  # other apps
    'django_mermaid.apps.MermaidConfig',
]
```

## Usage

After you configure the `INSTALLED_APPS`, you will be able to load the `mermaid` in your template and use the template
tag for rendering mermaid diagrams.

```jinja2
{% load mermaid %}
{% mermaid "graph LR; A-->B;" %}
```

### Mermaid version

By default, Django Mermaid uses the **9.4.3** version of mermaid. However, if you want to use a specific version of
mermaid, you can set the `MERMAID_VERSION` variable in your Django project's **settings.py** file.

```python
MERMAID_VERSION = '10.0.3-alpha.1'
```

Make sure the version you specify is available on the [mermaid CDN](https://cdnjs.com/libraries/mermaid), and has
the **mermaid.min.js** file.

### Mermaid theme

To set a default theme for the whole project, set the `MERMAID_THEME` variable in your Django project's **settings.py**
file. However, Django Mermaid uses
the [default](https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/themes/theme-default.js) theme of
mermaid by default. Also, check out the mermaid [docs](https://mermaid.js.org/config/theming.html?#theme-variables) for
the available themes.

```python
MERMAID_THEME = 'neutral'
```

Also, you can provide the theme right in the template tag which will dynamically override the value of
the `MERMAID_THEME` variable.

```jinja2
{% mermaid "graph LR; A-->B;" "dark" %}
```

### Mermaid theme variables

You can define your custom theme by overriding the `MERMAID_THEME_VARIABLES` variable. You will need to use
the [base](https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/themes/theme-base.js) theme as it is
the only modifiable theme. Check out the mermaid [docs](https://mermaid.js.org/config/theming.html?#theme-variables) for
the complete and up-to-date list of available theme variables.

```python
MERMAID_THEME_VARIABLES = {
    'primaryColor': '#BB2528',
    'primaryTextColor': '#FFF',
}
```

## Contribute

Any contribution is welcome. If you have any ideas or suggestions, feel free to open an issue or a pull request. And
don't forget to add tests for your changes.

## License

Copyright (C) 2023 Artyom Vancyan. [MIT](https://github.com/ArtyomVancyan/django-mermaid/blob/master/LICENSE)
