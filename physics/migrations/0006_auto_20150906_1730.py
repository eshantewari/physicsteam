# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0005_auto_20150906_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='file_url',
            new_name='filename',
        ),
        migrations.RenameField(
            model_name='pset',
            old_name='file_url',
            new_name='filename',
        ),
    ]
