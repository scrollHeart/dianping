# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0005_auto_20171119_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classfy',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('id', models.CharField(max_length=10, serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'T_classfy',
            },
        ),
    ]
