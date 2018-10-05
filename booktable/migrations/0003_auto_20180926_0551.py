# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktable', '0002_auto_20180926_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetails',
            name='cutomer_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
