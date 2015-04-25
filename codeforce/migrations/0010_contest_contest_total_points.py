# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0009_contestproblems_cp_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='contest_total_points',
            field=models.IntegerField(default=100),
        ),
    ]
