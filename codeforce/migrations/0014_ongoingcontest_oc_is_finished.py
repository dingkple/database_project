# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0013_auto_20150424_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='ongoingcontest',
            name='oc_is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
