# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0004_auto_20150422_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='contest_participant_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
