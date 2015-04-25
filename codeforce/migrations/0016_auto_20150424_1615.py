# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0015_auto_20150424_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestparticipantinfo',
            name='cpi_trial_time',
            field=models.DateTimeField(),
        ),
    ]
