from urllib.request import urlretrieve

from setuptools import setup

if __name__ == "__main__":
    urlretrieve(
        "https://cdnjs.cloudflare.com/ajax/libs/mermaid/9.4.3/mermaid.js",
        "src/django_mermaid/static/mermaid.js",
    )
    setup()
