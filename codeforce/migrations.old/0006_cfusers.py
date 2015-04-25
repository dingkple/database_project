# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0005_contest_contest_participant_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='CFUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_points', models.IntegerField()),
                ('user_contest_num', models.IntegerField()),
            ],
        ),
    ]
