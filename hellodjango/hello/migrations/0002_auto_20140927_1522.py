# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='legislator',
            name='house_history_id',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislator',
            name='terms_district',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='legislator',
            name='terms_class',
            field=models.IntegerField(default=-1),
        ),
    ]
