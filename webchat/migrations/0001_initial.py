# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 06:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_time', models.DateTimeField(auto_now=True, null=True)),
                ('content', models.CharField(blank=True, max_length=300, null=True)),
                ('already_read', models.IntegerField(choices=[(0, '\u672a\u8bfb'), (1, '\u5df2\u8bfb')], default=0)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cr', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
