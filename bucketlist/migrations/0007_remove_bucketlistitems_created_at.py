# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bucketlist', '0006_bucketlistitems_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bucketlistitems',
            name='created_at',
        ),
    ]
