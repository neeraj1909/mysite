# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterField(
            model_name='student',
            name='room_number',
            field=models.CharField(help_text='For example: A20', max_length=20, verbose_name='Room No.'),
        ),
    ]