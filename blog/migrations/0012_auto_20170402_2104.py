# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_case_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
