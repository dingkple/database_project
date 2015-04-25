# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0003_auto_20150422_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contest',
            old_name='contest_end_date',
            new_name='contest_end_time',
        ),
        migrations.RenameField(
            model_name='contest',
            old_name='contest_start_date',
            new_name='contest_start_time',
        ),
        migrations.AddField(
            model_name='contest',
            name='contest_publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 22, 17, 29, 44, 762959, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
