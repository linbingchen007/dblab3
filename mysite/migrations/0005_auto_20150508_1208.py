# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20150508_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='user',
            field=models.OneToOneField(related_name='promo', to='mysite.User'),
        ),
    ]
