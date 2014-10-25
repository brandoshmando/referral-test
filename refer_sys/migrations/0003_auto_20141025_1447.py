# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refer_sys', '0002_auto_20141025_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(max_length=200, unique=True),
            preserve_default=True,
        ),
    ]
