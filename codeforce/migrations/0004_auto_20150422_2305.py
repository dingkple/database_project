# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0003_auto_20150422_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestProblems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cp_trial_num', models.IntegerField()),
                ('cp_success_num', models.IntegerField()),
                ('contest', models.ForeignKey(to='codeforce.Contest')),
                ('contest_problem', models.ForeignKey(to='codeforce.Problem')),
            ],
        ),
        migrations.RemoveField(
            model_name='contestprblems',
            name='contest',
        ),
        migrations.RemoveField(
            model_name='contestprblems',
            name='contest_problem',
        ),
        migrations.DeleteModel(
            name='ContestPrblems',
        ),
    ]
