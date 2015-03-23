# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bucketlist', '0008_auto_20150316_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucketlistitems',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
