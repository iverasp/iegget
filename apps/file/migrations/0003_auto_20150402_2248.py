# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_auto_20150402_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='filetype',
            field=models.CharField(default=None, max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='file',
            name='size',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='file',
            name='link',
            field=models.CharField(default=None, max_length=255),
            preserve_default=True,
        ),
    ]
