# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0004_auto_20150403_0100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='link',
            new_name='uuid',
        ),
    ]
