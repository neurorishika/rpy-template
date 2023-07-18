# Rishika Python Project Template

This is a [Poetry](https://python-poetry.org/)-enabled template for Python projects for use by (Rishika Mohanta)[https://neurorishika.github.io].

Default settings are for Python 3.9 and above and the following packages are included:
- numpy
- pandas 
- matplotlib
- jupyter
- ipython
- scipy
- scikit-learn
- argparse
- mkinit
- cryptography
- lazy-loader


## Installation

Create a new project using this template on GitHub and clone it locally. Then, run the following commands in the project directory after installing Poetry:

```
cd <project directory>
python utils/quickstart.py
poetry install
```

## Update & Build Packages and Setup __init__.py for package with lazy imports

To update the packages and build the package, followed by setting up the __init__.py file for the package with lazy imports, run the following command:

```
poetry run python utils/build.py
```