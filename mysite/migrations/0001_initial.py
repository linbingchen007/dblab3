# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('categoryname', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Category_Film_Rel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fid', models.IntegerField(db_index=True)),
                ('cid', models.IntegerField(db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('covurl', models.CharField(default=b'', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ipaddr', models.CharField(max_length=25)),
                ('reged', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('picurl', models.CharField(max_length=100)),
                ('film', models.ForeignKey(to='mysite.Film')),
            ],
        ),
        migrations.CreateModel(
            name='Promourl',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('purl', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('tagname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tag_Film_Rel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fid', models.IntegerField(db_index=True)),
                ('tid', models.IntegerField(db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=75)),
                ('balance', models.IntegerField(default=0)),
                ('invites', models.IntegerField(default=0)),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vid',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('vidurl', models.CharField(max_length=100)),
                ('film', models.ForeignKey(to='mysite.Film')),
            ],
        ),
        migrations.AddField(
            model_name='promourl',
            name='user',
            field=models.OneToOneField(to='mysite.User'),
        ),
        migrations.AddField(
            model_name='ip',
            name='p_user',
            field=models.ForeignKey(to='mysite.User'),
        ),
    ]
