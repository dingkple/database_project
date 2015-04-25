# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0002_auto_20150422_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='contest_end_date',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='contest',
            name='contest_start_date',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='contestinfo',
            name='ci_trial_date',
            field=models.TimeField(),
        ),
    ]
