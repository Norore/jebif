# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bioinfuse', '0003_auto_20160417_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associatedkey',
            name='challenge',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='bioinfuse.Challenge'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='challenge',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='bioinfuse.Challenge'),
        ),
    ]
