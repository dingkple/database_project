# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0008_ongoingcontest'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestproblems',
            name='cp_points',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
