# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_notification_notification_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='subscriber_id',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
