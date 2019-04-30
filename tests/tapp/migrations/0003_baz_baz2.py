# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0002_auto_20170611_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tapp.Foo')),
            ],
        ),
        migrations.CreateModel(
            name='Baz2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tapp.Foo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
