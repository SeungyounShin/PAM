# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 14:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='schoolid',
            field=models.PositiveIntegerField(primary_key=True, validators=[django.core.validators.MaxValueValidator(99999)]),
        ),
    ]
