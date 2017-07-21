# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='User',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tracker.User'),
        ),
        migrations.AddField(
            model_name='goal',
            name='date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='subgoal',
            name='Goal',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tracker.Goal'),
        ),
        migrations.AddField(
            model_name='subgoal',
            name='date',
            field=models.DateField(default=None),
        ),
    ]
