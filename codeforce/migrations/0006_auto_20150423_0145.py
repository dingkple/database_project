# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0005_auto_20150423_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='publish_date',
            field=models.DateTimeField(),
        ),
    ]
