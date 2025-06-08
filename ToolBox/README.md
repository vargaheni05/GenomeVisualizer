# Example package
This is an example package with some dummy functions for use with the Scientific Python course (PPCU 2025)

> [!CAUTION]
> Please configure everything! This is just an example

## After writing your code

* Define your requirements
* Configure the `setup.py` and `pyproject.toml`
* Create `docs` with Sphinx
* Change the `LICENCE` if applicable
* Configure ReadTheDocs using `.readthedocs.yaml`
* Set up ReadTheDocs for your package
* Build, test, improve...
* Enjoy! 😎

## Building the package:
Editable mode install:
```console
pip install -e .
```
Install build:
```console
pip install build
```
Building the package:
```console
python -m build
```
This will create a `dist` directory with a source tarball and wheel file. These will be used to install your package.

## Documentation
### Creating and building the documentation:
Install Sphinx:
```console
pip install sphinx
```
Run "quickstart" and follow the prompts:
```console
sphinx-quickstart docs
```
Configure Sphinx in `conf.py`

Recommended extensions:
* `sphinx.ext.autodoc`
* `sphinx.ext.napoleon`
* `sphinx.ext.viewcode`

Recommended html theme: `sphinx_rtd_theme`

```console
pip install sphinx-rtd-theme
```

### Build documentation as local html:
Windows:
```console
./docs/make.bat html
```
Linux/Max:
```console
cd ./docs
make html
```
Manually:
```console
sphinx-build -M html <DOCS-SOURCE-PATH> <DOCS-BUILD-OUTPUT-PATH>
```