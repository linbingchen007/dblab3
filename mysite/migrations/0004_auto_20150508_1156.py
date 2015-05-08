# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20150508_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('invites', models.IntegerField(default=0)),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='clicks',
        ),
        migrations.RemoveField(
            model_name='user',
            name='invites',
        ),
        migrations.AddField(
            model_name='promo',
            name='user',
            field=models.OneToOneField(to='mysite.User'),
        ),
    ]
