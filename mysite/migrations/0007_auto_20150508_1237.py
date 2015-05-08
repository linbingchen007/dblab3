# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20150508_1230'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Film_User_Favorel',
            new_name='Film_User_Favrel',
        ),
    ]
