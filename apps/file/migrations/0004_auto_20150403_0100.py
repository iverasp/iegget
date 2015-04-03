# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0003_auto_20150402_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='filename',
            field=models.CharField(default=datetime.datetime(2015, 4, 2, 23, 0, 7, 239472, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='filetype',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='file',
            name='link',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
