# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codeforce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestProlbems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cp_trial_num', models.IntegerField()),
                ('cp_success_num', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='contestdetail',
            name='contest',
        ),
        migrations.RemoveField(
            model_name='contest',
            name='contest_problem',
        ),
        migrations.RemoveField(
            model_name='contest',
            name='cp_success_num',
        ),
        migrations.RemoveField(
            model_name='contest',
            name='cp_trial_num',
        ),
        migrations.AddField(
            model_name='contest',
            name='contest_creater',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contest',
            name='contest_description',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contest',
            name='contest_duration',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contest',
            name='contest_end_time',
            field=models.TimeField(default=datetime.datetime(2015, 4, 22, 22, 54, 13, 980440, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contest',
            name='contest_participant_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contest',
            name='contest_publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 22, 22, 54, 25, 336528, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contest',
            name='contest_start_time',
            field=models.TimeField(default=datetime.datetime(2015, 4, 22, 22, 54, 31, 259000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ContestDetail',
        ),
        migrations.AddField(
            model_name='contestprolbems',
            name='contest',
            field=models.ForeignKey(to='codeforce.Contest'),
        ),
        migrations.AddField(
            model_name='contestprolbems',
            name='contest_problem',
            field=models.ForeignKey(to='codeforce.Problem'),
        ),
    ]
