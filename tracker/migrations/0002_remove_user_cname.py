# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 21:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Cname',
        ),
    ]