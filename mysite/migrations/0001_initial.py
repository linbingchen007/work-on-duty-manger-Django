# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extrawork',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField(default=datetime.date(2015, 3, 13))),
                ('amname', models.CharField(max_length=75)),
                ('amtext', models.CharField(max_length=255)),
                ('amamount', models.IntegerField(default=0)),
                ('pmname', models.CharField(max_length=75)),
                ('pmtext', models.CharField(max_length=255)),
                ('pmamount', models.IntegerField(default=0)),
                ('evename', models.CharField(max_length=75)),
                ('evetext', models.CharField(max_length=255)),
                ('eveamount', models.IntegerField(default=0)),
                ('remark', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Registers',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField(default=datetime.date(2015, 3, 13))),
                ('amname', models.CharField(max_length=75)),
                ('amamount', models.IntegerField(default=0)),
                ('pmname', models.CharField(max_length=75)),
                ('pmamount', models.IntegerField(default=0)),
                ('evename', models.CharField(max_length=75)),
                ('eveamount', models.IntegerField(default=0)),
                ('remark', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
