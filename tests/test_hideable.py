from __future__ import unicode_literals

import os

import django
from django.test import TestCase

from .models import Hog


class TestHog(TestCase):

    def setUp(self):
        self.hog = Hog(name="Cochinardo")

    def test_hide(self):
        self.hog.hide()
