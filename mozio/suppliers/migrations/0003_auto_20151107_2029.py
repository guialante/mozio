# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_auto_20151107_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicearea',
            options={'get_latest_by': 'created'},
        ),
        migrations.AddField(
            model_name='servicearea',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 8, 4, 29, 8, 588394, tzinfo=utc), verbose_name='Date Created', auto_now_add=True),
            preserve_default=False,
        ),
    ]
