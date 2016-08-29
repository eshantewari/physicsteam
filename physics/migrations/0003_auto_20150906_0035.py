# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0002_topic_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='file_url',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pset',
            name='file_url',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
