# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bucketlist', '0002_auto_20150311_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='BucketListItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('finished', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='item',
            name='title',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.RemoveField(
            model_name='list',
            name='user',
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
