# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0010_lecture_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='lecture_file',
            field=models.FileField(default=0, upload_to=b'lectures'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pset',
            name='problems_file',
            field=models.FileField(default=0, upload_to=b'pset/problems'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pset',
            name='solutions_file',
            field=models.FileField(default=0, upload_to=b'pset/solutions'),
            preserve_default=False,
        ),
    ]
