# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bucketlist', '0005_remove_bucketlistitems_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucketlistitems',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=b'True'),
            preserve_default=True,
        ),
    ]
