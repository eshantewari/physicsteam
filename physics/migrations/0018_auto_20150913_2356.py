# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0017_suggestion_topicrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggestion',
            old_name='text',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='topicrequest',
            old_name='text',
            new_name='description',
        ),
        migrations.AddField(
            model_name='suggestion',
            name='title',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topicrequest',
            name='title',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
