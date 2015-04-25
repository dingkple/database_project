# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0016_auto_20150424_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestresults',
            name='cr_is_submited',
            field=models.BooleanField(default=False),
        ),
    ]
