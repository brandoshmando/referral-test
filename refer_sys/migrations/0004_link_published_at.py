# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('refer_sys', '0003_auto_20141025_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
