# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0010_contest_contest_total_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='ongoingcontest',
            name='oc_is_simulation',
            field=models.BooleanField(default=False),
        ),
    ]
