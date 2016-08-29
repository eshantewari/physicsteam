# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0003_auto_20150906_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='description',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pset',
            name='description',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
