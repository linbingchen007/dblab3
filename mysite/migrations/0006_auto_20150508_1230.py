# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20150508_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film_User_Favorel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fid', models.IntegerField(db_index=True, blank=True)),
                ('uid', models.IntegerField(db_index=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Film_User_Ownrel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fid', models.IntegerField(db_index=True, blank=True)),
                ('uid', models.IntegerField(db_index=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
