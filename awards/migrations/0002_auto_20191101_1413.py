# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-01 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rates',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='awards.Projects'),
        ),
    ]
