#coding:utf-8
from __future__ import unicode_literals
from django import forms
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(
        max_length=30,
        unique=True,
        error_messages = {
            'max_length':'用户名过长',
            'required':'用户名不能为空',
            'invalid':'输入类型错误'
        }
    )  
    password = models.CharField(
        max_length=30,
        error_messages = {
            'max_length':'密码过长',
            'required':'密码不能为空'
        }
    )  
    email = models.EmailField(
        error_messages={
            'required':'邮箱不能为空',
            'invalid':'邮箱规则不符合'
        }
    )
    tel = models.CharField(max_length=15)  
    # sex = models.CharField(max_length=10,null=True)  
    # name = models.CharField(max_length=15,null=True)  
    # age = models.IntegerField(null=True)
    nickname = models.CharField(max_length=30,null=True)
    myplan = models.ManyToManyField('Plan', related_name='+')
    myarticle = models.ManyToManyField('Plan', related_name='+')
    favoriteplan = models.ManyToManyField('Plan',related_name='+')
    favoritecase = models.ManyToManyField('Case',related_name='+')
    favoritearticle = models.ManyToManyField('Plan',related_name='+')

    def __unicode__(self):
        return self.username

class Case(models.Model):
    # caseid = models.DecimalField(max_digits=10, decimal_places=0)
    id = models.AutoField(primary_key=True)
    casename = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    # 推荐游玩时长
    hours = models.DecimalField(max_digits=2, decimal_places=1)
    # 第几天
    day = models.DecimalField(max_digits=2, decimal_places=0,default=1)
    description = models.TextField(null=True)
    CASETYPE_CHOICES = (
        ('food','吃'),
        ('shop','买'),
        ('play','玩'),
        ('view','景'),
        ('live','住'),
        ('other','其他'),
    )
    casetype = models.CharField(
        max_length=4,
        choices=CASETYPE_CHOICES,
        default='play'
    )
    def __unicode__(self):
        return self.casename

class Plan(models.Model):
    # planid = models.DecimalField(max_digits=8, decimal_places=0)
    id = models.AutoField(primary_key=True)
    PLANTYPE_CHOICES = (
        ('plan','行程'),
        ('article','游记'),
    )
    plantype=models.CharField(
        max_length=10,
        choices=PLANTYPE_CHOICES,
        default='plan')
    date=models.DateField(null=True)
    planname = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    makedate = models.DateField(auto_now_add=True)
    editdate = models.DateField(auto_now=True)
    days = models.DecimalField(max_digits=2, decimal_places=0)
    locations = models.CharField(max_length=30)
    cases = models.ManyToManyField(Case)
    description = models.TextField(null=True)
    def __unicode__(self):
        return self.planname
