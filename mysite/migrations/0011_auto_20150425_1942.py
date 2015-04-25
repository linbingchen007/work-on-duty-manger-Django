# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_auto_20150424_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dutyreg',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 25)),
        ),
        migrations.AlterField(
            model_name='extraworkreg',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 25)),
        ),
        migrations.AlterField(
            model_name='holidutyreg',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 25)),
        ),
    ]
