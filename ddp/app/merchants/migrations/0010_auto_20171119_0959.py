# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0009_classfyitem_parent_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchantitem',
            name='city',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='merchantitem',
            name='classfy',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='merchantitem',
            name='region',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='merchantitem',
            name='ave_price',
            field=models.FloatField(default=None, max_length=10),
        ),
    ]
