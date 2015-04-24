# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_holidutyreg_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dutyreg',
            name='amamount',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='dutyreg',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 24)),
        ),
        migrations.AlterField(
            model_name='dutyreg',
            name='eveamount',
            field=models.IntegerField(default=120),
        ),
        migrations.AlterField(
            model_name='dutyreg',
            name='pmamount',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='extraworkreg',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 24)),
        ),
        migrations.AlterField(
            model_name='holidutyreg',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 24)),
        ),
    ]
