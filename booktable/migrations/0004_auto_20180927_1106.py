# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktable', '0003_auto_20180926_0551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingdetails',
            old_name='cutomer_name',
            new_name='customer_name',
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]
