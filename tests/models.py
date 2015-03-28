import os

import django
from django.db import models

import trufflehog


class Hog(trufflehog.Hideable, models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        db_index=True,
        verbose_name="name",
    )
