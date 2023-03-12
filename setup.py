import os
from os.path import dirname, join
from urllib.request import urlretrieve

from setuptools import setup

if __name__ == "__main__":
    cdn = "https://cdnjs.cloudflare.com/ajax/libs/mermaid/9.4.3/mermaid.js"
    static = join(dirname(__file__), "src", "django_mermaid", "static")
    print("ls src\n\n")
    os.system("ls src")
    print("ls src/django_mermaid\n\n")
    os.system("ls src/django_mermaid")
    print("ls src/django_mermaid/static\n\n")
    os.system("ls src/django_mermaid/static")
    open(join(static, "mermaid.js"), "w").close()
    urlretrieve(cdn, join(static, "mermaid.js"))
    setup()
