# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subscriber_id', models.CharField(max_length=30)),
                ('browser_name', models.CharField(max_length=30)),
                ('browser_engine', models.CharField(max_length=30)),
                ('device', models.CharField(max_length=30)),
            ],
        ),
    ]
