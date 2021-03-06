# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-12 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bioinfuse', '0012_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='artistic_note',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, verbose_name='Artistique'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='captive_interest_note',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, verbose_name="Captive l'int\xe9r\xeat"),
        ),
        migrations.AlterField(
            model_name='vote',
            name='global_note',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, verbose_name='Globale'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='investment_note',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, verbose_name='Moyens investis'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='originality_note',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, verbose_name='Originalit\xe9 du sujet'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='rigorous_note',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, verbose_name='Rigueur scientifique'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='scientific_note',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, verbose_name='Scientifique'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='take_home_message_note',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, verbose_name='Take-home message'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='understandable_note',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, verbose_name='Compr\xe9hensible par la cible'),
        ),
    ]
