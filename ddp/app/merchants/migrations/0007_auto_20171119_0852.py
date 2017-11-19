# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0006_classfy'),
    ]

    operations = [

        migrations.CreateModel(
            name='RegionItem',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('id', models.CharField(max_length=10, serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'T_region',
            },
        ),
        migrations.RenameModel(
            old_name='Classfy',
            new_name='ClassfyItem',
        ),
        migrations.RenameModel(
            old_name='MerchantInfo',
            new_name='MerchantItem',
        ),
    ]
