# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subscribes',
            field=models.ManyToManyField(verbose_name='Подписки', to=settings.AUTH_USER_MODEL),
        ),
    ]
