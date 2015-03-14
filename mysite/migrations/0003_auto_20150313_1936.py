# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20150313_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('varname', models.CharField(max_length=255)),
                ('varval', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='dutyreg',
            name='amname',
            field=models.CharField(default=b' ', max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dutyreg',
            name='evename',
            field=models.CharField(default=b' ', max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dutyreg',
            name='pmname',
            field=models.CharField(default=b' ', max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dutyreg',
            name='remark',
            field=models.CharField(default=b' ', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='extraworkreg',
            name='amname',
            field=models.CharField(default=b' ', max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='extraworkreg',
            name='amtext',
            field=models.CharField(default=b' ', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='extraworkreg',
            name='evename',
            field=models.CharField(default=b' ', max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='extraworkreg',
            name='evetext',
            field=models.CharField(default=b' ', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='extraworkreg',
            name='pmname',
            field=models.CharField(default=b' ', max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='extraworkreg',
            name='pmtext',
            field=models.CharField(default=b' ', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='extraworkreg',
            name='remark',
            field=models.CharField(default=b' ', max_length=255),
            preserve_default=True,
        ),
    ]
