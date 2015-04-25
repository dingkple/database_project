# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
            ],
        ),
    ]
