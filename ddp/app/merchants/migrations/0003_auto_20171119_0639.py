# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0002_auto_20171119_0610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchantinfo',
            name='shop_id',
        ),
        migrations.AddField(
            model_name='merchantinfo',
            name='detail_url',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='merchantinfo',
            name='img_url',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='merchantinfo',
            name='address',
            field=models.CharField(default=None, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='merchantinfo',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='merchantinfo',
            name='phone',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]
