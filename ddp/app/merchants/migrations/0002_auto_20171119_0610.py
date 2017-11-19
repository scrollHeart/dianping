# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchantinfo',
            name='address',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='merchantinfo',
            name='ave_price',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='merchantinfo',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='merchantinfo',
            name='phone',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='merchantinfo',
            name='shop_id',
            field=models.IntegerField(default=None),
        ),
    ]
