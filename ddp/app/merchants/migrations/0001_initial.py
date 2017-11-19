# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MerchantInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(default=None, max_length=20)),
                ('name', models.CharField(default=None, max_length=30)),
                ('huanjing', models.FloatField(default=0)),
                ('fuwu', models.FloatField(default=0)),
                ('kouwei', models.FloatField(default=0)),
                ('tag', models.CharField(default=None, max_length=20)),
            ],
            options={
                'db_table': 'T_merchants',
            },
        ),
    ]
