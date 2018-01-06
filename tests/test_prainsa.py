#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `prainsa` package."""


import unittest

from prainsa import prainsa


class TestPrainsa(unittest.TestCase):
    """Tests for `prainsa` package."""

    def setUp(self):
        prainsa.main()
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def test_000_something(self):
        """Test something."""
        pass
