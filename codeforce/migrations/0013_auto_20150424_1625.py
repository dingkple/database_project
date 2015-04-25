# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0012_auto_20150424_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cfusers',
            name='user_gender',
            field=models.CharField(default=b'M', max_length=1),
        ),
    ]
