# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Event(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField()
    description=models.TextField()

    def __str__(self):
        return self.title

