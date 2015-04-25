# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0011_ongoingcontest_oc_is_simulation'),
    ]

    operations = [
        migrations.AddField(
            model_name='cfusers',
            name='user_gender',
            field=models.CharField(default=2, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cfusers',
            name='user_location',
            field=models.CharField(default='MA', max_length=100),
            preserve_default=False,
        ),
    ]
