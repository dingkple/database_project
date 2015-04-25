# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0006_auto_20150423_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='contest_name',
            field=models.CharField(default='contest name', max_length=200),
            preserve_default=False,
        ),
    ]
