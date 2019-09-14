#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `nefnir` package."""

import unittest

from nefnir import lemmatize, lemmatize_line, recase


class TestNefnir(unittest.TestCase):
    """Tests for `nefnir` package."""

    def test_lemmatize(self):
        self.assertEqual('hver', lemmatize('Hvað', 'fshen'))

    def test_recase(self):
        self.assertEqual('DNA-þráður', recase('DNA-þræðinum', 'nkeþgs', 'dna-þráður'))

    def test_lemmatize_line(self):
        self.assertEqual(('Hvað', 'fshen', 'hver'), lemmatize_line('Hvað fshen', separator=' '))
        self.assertEqual('taka', lemmatize_line('tóku\tsfg3fþ')[2])
        self.assertEqual('Vestur-Íslendingur', lemmatize_line('Vestur-Íslendingarnir\tnkfng', separator='\t')[2])
