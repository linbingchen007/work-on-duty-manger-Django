# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20150318_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holidutyreg',
            name='date',
        ),
    ]
