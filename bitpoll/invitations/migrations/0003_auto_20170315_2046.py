# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitations', '0002_auto_20170310_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='last_invited',
        ),
        migrations.AddField(
            model_name='invitation',
            name='last_email',
            field=models.DateTimeField(null=True),
        ),
    ]
