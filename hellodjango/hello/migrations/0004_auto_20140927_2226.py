# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20140927_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('terms_type', models.CharField(max_length=8)),
                ('terms_start', models.DateField()),
                ('terms_end', models.DateField()),
                ('terms_state', models.CharField(max_length=2)),
                ('terms_class', models.IntegerField(default=-1)),
                ('terms_party', models.CharField(max_length=32)),
                ('terms_district', models.IntegerField(default=-1)),
                ('bioguide_id', models.ForeignKey(to='hello.Legislator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='legislator',
            name='terms_class',
        ),
        migrations.RemoveField(
            model_name='legislator',
            name='terms_district',
        ),
        migrations.RemoveField(
            model_name='legislator',
            name='terms_end',
        ),
        migrations.RemoveField(
            model_name='legislator',
            name='terms_party',
        ),
        migrations.RemoveField(
            model_name='legislator',
            name='terms_start',
        ),
        migrations.RemoveField(
            model_name='legislator',
            name='terms_state',
        ),
        migrations.RemoveField(
            model_name='legislator',
            name='terms_type',
        ),
    ]
