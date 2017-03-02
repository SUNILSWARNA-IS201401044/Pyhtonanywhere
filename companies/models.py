from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Stock1(models.Model):
    data=models.TextField(
        db_column='data',
        blank=True)
    desc= models.TextField(blank=True)
    def __str__(self):
        return self.desc

