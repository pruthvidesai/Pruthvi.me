# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0004_creator_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creator',
            name='slug',
        ),
    ]
