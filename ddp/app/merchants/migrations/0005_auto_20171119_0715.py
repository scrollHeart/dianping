# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0004_auto_20171119_0711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchantinfo',
            old_name='comment',
            new_name='star',
        ),
    ]
