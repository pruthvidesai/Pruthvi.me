# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0002_auto_20150201_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='published',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
