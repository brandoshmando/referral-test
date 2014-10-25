# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('refer_sys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='link',
            name='clicks',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
