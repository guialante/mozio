# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('area', django.contrib.gis.db.models.fields.PolygonField(srid=4326, verbose_name='Area')),
                ('user', models.ForeignKey(related_name='service_areas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
