# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_plan_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
    ]