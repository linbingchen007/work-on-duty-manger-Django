# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_remove_holidutyreg_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='holidutyreg',
            name='date',
            field=models.DateField(default=datetime.date(2015, 3, 18)),
            preserve_default=True,
        ),
    ]
