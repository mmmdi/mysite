# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_plan_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plan',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
