# -*- coding: utf-8 -*-
import pkgutil
import json

from typing import Optional, Tuple

from .nefnir import Nefnir as _Nefnir


class _NefnirPackage(_Nefnir):
    def __init__(self, rules, tagmap):
        # Load resources from package
        self.rules = rules
        self.tagmap = tagmap

        self.proper = {t for t in self.tagmap if t[0] == 'n' and t[-1] in {'m', 'ö', 's'}}
        self.unanalyzed = {t for t in self.tagmap if t[:2] == 'nx'} | {'x', 'e', 'as'}


_nefnir: Optional[_NefnirPackage] = None


def _get_nefnir() -> _NefnirPackage:
    if _nefnir is None:
        init()
    assert _nefnir is not None, "Failed initalization"
    return _nefnir


def init() -> None:
    """Read configuration files."""
    global _nefnir
    rule_data = pkgutil.get_data(__package__, 'rules.json')
    tag_data = pkgutil.get_data(__package__, 'tags.json')
    if rule_data is not None and tag_data is not None:
        rules = json.loads(rule_data)
        tagmap = json.loads(tag_data)

        _nefnir = _NefnirPackage(rules, tagmap)


def lemmatize(form: str, tag: str) -> str:
    """
    Lemmatize a word form given its part-of-speech tag.

    :param form: A word form.
    :param tag: The word form's part-of-speech tag.
    :return: The word form's lemma.
    """
    return _get_nefnir().lemmatize(form, tag)


def recase(form: str, tag: str, lemma: str) -> str:
    """
    Determine how to properly case a lemma given the word form and part of speech tag it was derived from.

    Nefnir transforms words into lowercase prior to lemmatization. Some words, such as proper nouns, abbreviations
    and foreign words therefore need to be re-capitalized or changed back into uppercase.

    :param form: A word form, cased as it was written.
    :param tag: The word form's part-of-speech tag.
    :param lemma: The word form's lemma, in lowercase.
    :return: A properly cased lemma.
    """
    return _get_nefnir().recase(form, tag, lemma)


def lemmatize_line(line: str, separator: str = '\t') -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Lemmatize a word form given its part-of-speech tag.

    :param line: A line with form and tag separated by seperator.
    :param separator: The token separator.
    :return: Tuple with form, tag, lemma (any can be None if data invalid).
    """
    form = None
    tag = None
    lemma = None

    line = line.strip()
    if len(line) > 0:
        if separator in line:
            form, tag = line.split(separator)
            lemma = lemmatize(form, tag)
    return form, tag, lemma
