# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_auto_20140927_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='legislator',
            name='ballotpedia_id',
            field=models.CharField(default=b'none', max_length=48),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislator',
            name='cspan_id',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislator',
            name='maplight_id',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislator',
            name='opensecrets_id',
            field=models.CharField(default=-1, max_length=16),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislator',
            name='thomas_id',
            field=models.CharField(default=b'none', max_length=8),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislator',
            name='votesmart_id',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislator',
            name='washington_post_id',
            field=models.CharField(default=b'none', max_length=16),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='legislator',
            name='wikipedia_id',
            field=models.CharField(default=b'none', max_length=48),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='terms',
            name='bioguide_id',
            field=models.ForeignKey(to='hello.Legislator'),
        ),
    ]
