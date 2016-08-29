# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0012_auto_20150906_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecture_file',
            field=models.FileField(null=True, upload_to=b'lectures', blank=True),
        ),
        migrations.AlterField(
            model_name='pset',
            name='problems_file',
            field=models.FileField(null=True, upload_to=b'pset/problems', blank=True),
        ),
        migrations.AlterField(
            model_name='pset',
            name='solutions_file',
            field=models.FileField(null=True, upload_to=b'pset/solutions', blank=True),
        ),
    ]
