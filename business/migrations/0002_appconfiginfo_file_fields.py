# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-01 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appconfiginfo',
            name='file_fields',
            field=models.CharField(blank=True, help_text='文件字段配置项，#号隔开', max_length=128, null=True, verbose_name='文件字段'),
        ),
    ]
