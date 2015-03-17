# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0003_creator_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 2, 1, 20, 12, 35, 223000, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
