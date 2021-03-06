# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-26 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('owner', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('contract_no', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
