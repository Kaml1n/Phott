# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import gallery.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', gallery.fields.ThumbnailImageField(upload_to='photos')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Categories')),
            ],
            options={
                'ordering': ['time_stamp'],
            },
        ),
    ]
