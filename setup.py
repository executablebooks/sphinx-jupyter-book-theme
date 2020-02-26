"""Sphinx Bootstrap Theme package."""
from setuptools import setup


setup(
    name="sphinx-jupyter-book-theme",
    version="0.0.1.dev0",
    description="Sphinx Bootstrap Theme - pandas version.",
    url="https://github.com/pandas-dev/pandas-sphinx-theme",
    #
    packages=["sphinx_jupyter_book_theme"],
    package_data={
        "sphinx_jupyter_book_theme": [
            "theme.conf",
            "*.html",
            "static/sphinx-bootstrap.css_t",
            "static/css/*.css",
            "static/js/*.js",
            "static/img/*",
        ]
    },
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points={"sphinx.html_themes": ["sphinx_jupyter_book_theme = sphinx_jupyter_book_theme"]},
    install_requires=[
        "sphinx",
        (
            "myst-nb @ "
            "https://github.com/ExecutableBookProject/MyST-NB/archive/master.zip"
        ),
        "ipython",
        "ipywidgets"
    ],
)
