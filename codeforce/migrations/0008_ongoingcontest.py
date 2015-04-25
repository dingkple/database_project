# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0007_contest_contest_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='OngoingContest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oc_start_time', models.DateTimeField()),
                ('oc_end_time', models.DateTimeField()),
                ('oc_points', models.IntegerField()),
                ('oc_contest', models.ForeignKey(to='codeforce.Contest')),
                ('oc_user', models.ForeignKey(to='codeforce.CFUsers')),
            ],
        ),
    ]
