# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0004_auto_20150422_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='contest_publish_date',
        ),
        migrations.AlterField(
            model_name='contest',
            name='contest_end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contest',
            name='contest_start_time',
            field=models.DateTimeField(),
        ),
    ]
