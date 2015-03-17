# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0005_remove_creator_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='external',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
