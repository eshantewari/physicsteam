# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0004_auto_20150906_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pset',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
