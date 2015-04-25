# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contest_creater', models.CharField(max_length=100)),
                ('contest_duration', models.IntegerField()),
                ('contest_start_date', models.DateField()),
                ('contest_end_date', models.DateField()),
                ('contest_problem_list_id', models.IntegerField()),
                ('contest_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ContestInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ci_cid', models.IntegerField()),
                ('ci_pid', models.IntegerField()),
                ('ci_uid', models.IntegerField()),
                ('ci_is_right', models.BooleanField()),
                ('ci_trial_date', models.DateField()),
                ('ci_trial_answer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ContestProblemList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpl_cid', models.IntegerField()),
                ('cpl_pid', models.IntegerField()),
                ('cpl_trial_num', models.IntegerField()),
                ('cpl_success_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ContestResults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cr_cid', models.IntegerField()),
                ('cr_uid', models.IntegerField()),
                ('cr_points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='friends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.IntegerField()),
                ('fid', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='contest_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='trial_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
