# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0005_auto_20150403_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='mimetype',
            field=models.CharField(default='fdsfs', max_length=255),
            preserve_default=False,
        ),
    ]
