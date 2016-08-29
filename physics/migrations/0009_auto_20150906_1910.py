# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0008_auto_20150906_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='description',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='pset',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='pset',
            name='solution_filename',
        ),
    ]
