# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-25 23:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hptrivia_app', '0002_auto_20161225_2258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='answer1_text',
            new_name='correct_answer_text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='answer2_text',
            new_name='wrong_answer1_text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='answer3_text',
            new_name='wrong_answer2_text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='answer4_text',
            new_name='wrong_answer3_text',
        ),
    ]