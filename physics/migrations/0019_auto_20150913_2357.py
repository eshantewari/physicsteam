# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0018_auto_20150913_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='topicrequest',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
