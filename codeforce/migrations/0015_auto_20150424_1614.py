# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0014_ongoingcontest_oc_is_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestparticipantinfo',
            name='cpi_trial_date',
        ),
        migrations.AlterField(
            model_name='contestparticipantinfo',
            name='cpi_trial_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 16, 14, 36, 332694)),
        ),
    ]
