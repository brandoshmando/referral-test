# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refer_sys', '0004_link_published_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='published_at',
        ),
    ]
