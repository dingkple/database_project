# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cp_trial_num', models.IntegerField()),
                ('cp_success_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ContestDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contest_creater', models.CharField(max_length=100)),
                ('contest_duration', models.IntegerField()),
                ('contest_start_time', models.TimeField()),
                ('contest_end_time', models.TimeField()),
                ('contest_publish_date', models.DateField()),
                ('contest_description', models.CharField(max_length=500)),
                ('contest_participant_num', models.IntegerField()),
                ('contest', models.ForeignKey(to='codeforce.Contest')),
            ],
        ),
        migrations.CreateModel(
            name='ContestParticipantInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpi_is_right', models.BooleanField()),
                ('cpi_trial_time', models.TimeField()),
                ('cpi_trial_date', models.DateField()),
                ('cpi_trial_answer', models.IntegerField()),
                ('cpi_contest', models.ForeignKey(to='codeforce.Contest')),
            ],
        ),
        migrations.CreateModel(
            name='ContestResults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cr_points', models.IntegerField()),
                ('cr_contest', models.ForeignKey(to='codeforce.Contest')),
                ('cr_user', models.ForeignKey(to='codeforce.CFUsers')),
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
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problem_title', models.CharField(max_length=100)),
                ('publish_date', models.DateField()),
                ('solved_num', models.IntegerField()),
                ('difficulty_type', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=100)),
                ('trial_num', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='contestparticipantinfo',
            name='cpi_problem',
            field=models.ForeignKey(to='codeforce.Problem'),
        ),
        migrations.AddField(
            model_name='contestparticipantinfo',
            name='cpi_user',
            field=models.ForeignKey(to='codeforce.CFUsers'),
        ),
        migrations.AddField(
            model_name='contest',
            name='contest_problem',
            field=models.ForeignKey(to='codeforce.Problem'),
        ),
    ]
