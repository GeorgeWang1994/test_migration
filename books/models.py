#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    george wang
@datetime:  2019-05-23
@file:      models.py
@contact:   georgewang1994@163.com
@desc:      ...
"""


from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=100, verbose_name="书的名字")
    desc = models.CharField(max_length=200, verbose_name="书的简介")
    type = models.CharField(max_length=10, default='first', choices=[('first', 'first'), ('second', 'second')], verbose_name="类型")
    content = models.TextField(default="", verbose_name="书的内容")
    created_time = models.DateTimeField(null=True, auto_now_add=True, verbose_name="创建时间")


class Publish(models.Model):
    name = models.CharField(max_length=100, verbose_name="出版商的名字")
    desc = models.CharField(max_length=200, default="", verbose_name="书的简介")
    created_time = models.DateTimeField(null=True, auto_now_add=True, verbose_name="创建时间")
