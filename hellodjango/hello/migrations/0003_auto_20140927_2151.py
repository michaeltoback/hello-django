# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20140927_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legislator',
            name='id',
        ),
        migrations.AlterField(
            model_name='legislator',
            name='bioguide_id',
            field=models.CharField(max_length=8, serialize=False, primary_key=True),
        ),
    ]
