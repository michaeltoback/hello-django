# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_auto_20140928_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legislator',
            name='washington_post_id',
            field=models.CharField(default=b'none', max_length=48),
        ),
        migrations.AlterField(
            model_name='terms',
            name='bioguide_id',
            field=models.ForeignKey(to='hello.Legislator'),
        ),
    ]
