========
capsules
========

Python library for depositing a function definition inside a temporary module file (mostly for use with multiprocessing and Jupyter Notebook).

|pypi|

.. |pypi| image:: https://badge.fury.io/py/capsules.svg
   :target: https://badge.fury.io/py/capsules
   :alt: PyPI version and link.

Package Installation and Usage
------------------------------
The package is available on PyPI::

    python -m pip install capsules

The library can be imported in the usual ways::

    import capsules
    from capsules import capsules

Adding the `capsules` decorator to a function definition will (1) automatically deposit that definition inside a temporary module file on disk, (2) import that module file, and (3) assign to the variable of the function being defined the function that was imported from that module::

    @capsules
    def double(x):
        return x + x

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the GitHub page for this library.

Versioning
----------
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`_.
