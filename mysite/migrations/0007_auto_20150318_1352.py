# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20150314_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holidutyreg',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField(default=datetime.date(2015, 3, 18))),
                ('emergencyteamname', models.CharField(max_length=75)),
                ('emergencyteamamount', models.IntegerField(default=0)),
                ('servicecentername', models.CharField(max_length=75)),
                ('servicecenteramount', models.IntegerField(default=0)),
                ('generaldutyname', models.CharField(max_length=75)),
                ('generaldutyamount', models.IntegerField(default=0)),
                ('amphonedutyname', models.CharField(max_length=75)),
                ('amphonedutyamount', models.IntegerField(default=0)),
                ('amengineername', models.CharField(max_length=75)),
                ('amengineeramount', models.IntegerField(default=0)),
                ('pmphonedutyname', models.CharField(max_length=75)),
                ('pmphonedutyamount', models.IntegerField(default=0)),
                ('pmengineername', models.CharField(max_length=75)),
                ('pmengineeramount', models.IntegerField(default=0)),
                ('evedutyname', models.CharField(max_length=75)),
                ('evedutyamount', models.IntegerField(default=0)),
                ('remark', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='dutyreg',
            name='date',
            field=models.DateField(default=datetime.date(2015, 3, 18)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='extraworkreg',
            name='date',
            field=models.DateField(default=datetime.date(2015, 3, 18)),
            preserve_default=True,
        ),
    ]
