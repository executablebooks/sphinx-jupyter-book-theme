# sphinx-jupyter-book-theme

✨✨EXPERIMENTAL✨✨

This is an experimental theme to try replicating the general Jupyter Book theme (jupyterbook.org)
using Bootstrap and Sphinx as a build engine. It will evolve rapidly and is not guaranteed to
remain stable (or to exist at all!)

It is **heavily** inspired from the pydata sphinx bootstrap theme: https://github.com/pandas-dev/pydata-bootstrap-sphinx-theme
and uses [nbsphinx](https://nbsphinx.readthedocs.io/en/0.5.0/) to read in notebooks to Sphinx.

## Installation

```bash
pip install -e .
```

and then

```bash
cd docs/make html
```