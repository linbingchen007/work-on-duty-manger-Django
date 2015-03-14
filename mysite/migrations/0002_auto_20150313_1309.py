# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registers',
            new_name='Dutyreg',
        ),
        migrations.RenameModel(
            old_name='Extrawork',
            new_name='Extraworkreg',
        ),
    ]
