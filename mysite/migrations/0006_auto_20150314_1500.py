# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20150313_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dutyreg',
            name='date',
            field=models.DateField(default=datetime.date(2015, 3, 14)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='extraworkreg',
            name='date',
            field=models.DateField(default=datetime.date(2015, 3, 14)),
            preserve_default=True,
        ),
    ]
