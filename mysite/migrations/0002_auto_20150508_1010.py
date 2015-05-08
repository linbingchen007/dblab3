# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=15, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='promourl',
            name='user',
        ),
        migrations.AlterField(
            model_name='category',
            name='categoryname',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='category_film_rel',
            name='cid',
            field=models.IntegerField(db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='category_film_rel',
            name='fid',
            field=models.IntegerField(db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='pic',
            name='picurl',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tagname',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='tag_film_rel',
            name='fid',
            field=models.IntegerField(db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tag_film_rel',
            name='tid',
            field=models.IntegerField(db_index=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=75, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=25, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=25, blank=True),
        ),
        migrations.AlterField(
            model_name='vid',
            name='vidurl',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.DeleteModel(
            name='Promourl',
        ),
    ]
