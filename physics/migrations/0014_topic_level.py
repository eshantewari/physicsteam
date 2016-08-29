# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0013_auto_20150906_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='level',
            field=models.IntegerField(default=0, choices=[(0, b'Both'), (1, b'Experimental'), (2, b'Theoretical')]),
        ),
    ]
