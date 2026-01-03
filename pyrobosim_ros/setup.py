"""Legacy shim for setuptools while metadata is stored in pyproject.toml.

This file is intentionally small to keep backward compatibility with
installers that execute setup.py. The canonical project metadata is in
`pyproject.toml` (PEP 621).
"""

from setuptools import setup


if __name__ == "__main__":
    # Delegate to setuptools; the metadata will be read from pyproject.toml
    setup()
