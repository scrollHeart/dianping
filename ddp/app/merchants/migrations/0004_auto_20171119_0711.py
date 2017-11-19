# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0003_auto_20171119_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchantinfo',
            name='img_url',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]
