# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0014_topic_level'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecture_file',
            field=models.FileField(upload_to='lectures', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='level',
            field=models.IntegerField(default=0, choices=[(0, 'Both'), (1, 'Experimental'), (2, 'Theoretical')]),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='pset',
            name='level',
            field=models.IntegerField(default=0, choices=[(0, 'Both'), (1, 'Experimental'), (2, 'Theoretical')]),
        ),
        migrations.AlterField(
            model_name='pset',
            name='problems_file',
            field=models.FileField(upload_to='pset/problems', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pset',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='pset',
            name='solutions_file',
            field=models.FileField(upload_to='pset/solutions', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='level',
            field=models.IntegerField(default=0, choices=[(0, 'Both'), (1, 'Experimental'), (2, 'Theoretical')]),
        ),
        migrations.AlterField(
            model_name='topic',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
