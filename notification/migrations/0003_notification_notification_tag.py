# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notification_tag',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
