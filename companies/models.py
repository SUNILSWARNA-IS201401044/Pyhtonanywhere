from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Stock(models.Model):
    data=models.TextField(
        db_column='data',
        blank=True)


    desc= models.TextField(blank=True)
    imgid = models.AutoField(primary_key=True,default=1)

    def _str_(self):
        return self.imgid

