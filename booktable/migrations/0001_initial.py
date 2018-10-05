# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookingdetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cutomer_name', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('date', models.DateField()),
                ('email', models.EmailField(max_length=50)),
                ('number_of_guest', models.CharField(max_length=6)),
                ('time', models.TextField()),
            ],
        ),
    ]
