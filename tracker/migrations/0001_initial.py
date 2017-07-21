# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SubGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pname', models.CharField(default='Test', max_length=128)),
                ('Cname', models.CharField(default='Test', max_length=128)),
                ('UID', models.CharField(default='Test', max_length=128)),
                ('PicUrl', models.URLField(default='http://ksmart.herokuapp.com')),
                ('PhoneNumber', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]