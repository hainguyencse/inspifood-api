# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-31 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='food',
        ),
        migrations.AddField(
            model_name='place',
            name='food',
            field=models.ManyToManyField(blank=True, related_name='place_foods', to='api.Food'),
        ),
    ]
