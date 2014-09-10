# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='slug',
            field=models.SlugField(default=5, unique=True, max_length=200),
            preserve_default=False,
        ),
    ]
