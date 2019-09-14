"""Top-level package for nefnir (nefnir-package)."""

__author__ = """Sverrir Á. Berg"""
__email__ = 'sab@keilir.com'
__version__ = '1.0.2'

__all__ = [
    "init",
    "lemmatize",
    "lemmatize_line",
    "recase",
]

from .wrapper import init, lemmatize, lemmatize_line, recase
