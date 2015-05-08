# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20150508_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='variable',
            name='val',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='variable',
            name='name',
            field=models.CharField(db_index=True, max_length=15, blank=True),
        ),
    ]
