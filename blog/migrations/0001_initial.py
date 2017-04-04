# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseid', models.DecimalField(decimal_places=0, max_digits=10)),
                ('casename', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('hours', models.DecimalField(decimal_places=1, max_digits=2)),
                ('description', models.TextField()),
                ('casetype', models.CharField(choices=[('food', '\u5403'), ('shop', '\u4e70'), ('play', '\u73a9'), ('view', '\u666f'), ('live', '\u4f4f'), ('other', '\u5176\u4ed6')], default='play', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planname', models.CharField(max_length=30)),
                ('makedate', models.DateField(auto_now_add=True)),
                ('editdate', models.DateField(auto_now=True)),
                ('days', models.DecimalField(decimal_places=0, max_digits=2)),
                ('locations', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(error_messages={'invalid': '\u8f93\u5165\u7c7b\u578b\u9519\u8bef', 'max_length': '\u7528\u6237\u540d\u8fc7\u957f', 'required': '\u7528\u6237\u540d\u4e0d\u80fd\u4e3a\u7a7a'}, max_length=30, unique=True)),
                ('password', models.CharField(error_messages={'max_length': '\u5bc6\u7801\u8fc7\u957f', 'required': '\u5bc6\u7801\u4e0d\u80fd\u4e3a\u7a7a'}, max_length=30)),
                ('email', models.EmailField(error_messages={'invalid': '\u90ae\u7bb1\u89c4\u5219\u4e0d\u7b26\u5408', 'required': '\u90ae\u7bb1\u4e0d\u80fd\u4e3a\u7a7a'}, max_length=254)),
                ('tel', models.CharField(max_length=15)),
                ('sex', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=15, null=True)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='plan',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
        ),
        migrations.AddField(
            model_name='plan',
            name='cases',
            field=models.ManyToManyField(to='blog.Case'),
        ),
    ]