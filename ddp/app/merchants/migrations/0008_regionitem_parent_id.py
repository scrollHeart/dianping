# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0007_auto_20171119_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionitem',
            name='parent_id',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]
