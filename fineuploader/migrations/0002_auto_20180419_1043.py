# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-19 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import fineuploader.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('fineuploader', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temporary',
            name='id',
        ),
        migrations.AlterField(
            model_name='temporary',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
