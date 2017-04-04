# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_plan_plantype'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favoritearticle',
            field=models.ManyToManyField(related_name='_user_favoritearticle_+', to='blog.Plan'),
        ),
        migrations.AddField(
            model_name='user',
            name='favoritecase',
            field=models.ManyToManyField(related_name='_user_favoritecase_+', to='blog.Case'),
        ),
        migrations.AddField(
            model_name='user',
            name='favoriteplan',
            field=models.ManyToManyField(related_name='_user_favoriteplan_+', to='blog.Plan'),
        ),
    ]