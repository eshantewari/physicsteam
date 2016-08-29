# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0019_auto_20150913_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='pset',
            name='solutions_description',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
