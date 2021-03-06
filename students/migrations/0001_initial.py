# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80, verbose_name='Full Name')),
                ('age', models.PositiveIntegerField(verbose_name='Age')),
                ('room_number', models.CharField(max_length=20, verbose_name='Room No.')),
                ('hostel', models.CharField(max_length=80, verbose_name='Hostel')),
                ('hometown', models.CharField(max_length=80, verbose_name='Hometown')),
            ],
            options={
                'verbose_name': 'Neeraj ke app waala ek student',
                'verbose_name_plural': 'Dher Saare Bachche!',
            },
        ),
    ]
