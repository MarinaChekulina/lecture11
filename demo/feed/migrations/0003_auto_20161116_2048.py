# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20161110_1009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'посты', 'verbose_name': 'пост'},
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(verbose_name='Дата создания', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(verbose_name='Кто запостил', to=settings.AUTH_USER_MODEL),
        ),
    ]
