# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notification_title', models.CharField(max_length=200)),
                ('notification_url', models.URLField()),
                ('notification_message', models.CharField(max_length=200)),
            ],
        ),
    ]
