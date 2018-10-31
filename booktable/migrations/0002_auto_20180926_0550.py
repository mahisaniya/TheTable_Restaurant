# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetails',
            name='cutomer_name',
            field=models.CharField(default=b'name', max_length=50),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='email',
            field=models.EmailField(max_length=50, blank=True),
        ),
    ]
