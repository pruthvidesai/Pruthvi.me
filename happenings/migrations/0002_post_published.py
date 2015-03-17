# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
