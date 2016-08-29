# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0020_pset_solutions_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='description',
            field=models.CharField(default=b'', max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pset',
            name='description',
            field=models.CharField(default=b'', max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pset',
            name='solutions_description',
            field=models.CharField(default=b'', max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.CharField(default=b'', max_length=1000, null=True, blank=True),
        ),
    ]
