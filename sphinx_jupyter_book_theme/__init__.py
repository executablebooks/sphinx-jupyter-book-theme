"""
Sphinx Bootstrap theme.

Adapted for the pandas documentation.
"""
import os
from pathlib import Path
import sphinx.builders.html
import docutils

__version__ = "0.0.1.dev0"


def get_html_theme_path():
    """Return list of HTML theme paths."""
    theme_path = os.path.abspath(os.path.dirname(__file__))
    return [theme_path]


def setup(app):
    from pandas_sphinx_theme import setup
    setup(app)

    theme_path = get_html_theme_path()[0]
    app.add_html_theme("sphinx_jupyter_book_theme", theme_path)
