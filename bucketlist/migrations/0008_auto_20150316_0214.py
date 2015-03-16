# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bucketlist', '0007_remove_bucketlistitems_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketlistitems',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
