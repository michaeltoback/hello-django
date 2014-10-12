# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='legislator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bioguide_id', models.CharField(max_length=8)),
                ('govtrack_id', models.IntegerField()),
                ('icpsr_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('bio_birthday', models.DateField()),
                ('bio_gender', models.CharField(max_length=1)),
                ('terms_type', models.CharField(max_length=8)),
                ('terms_start', models.DateField()),
                ('terms_end', models.DateField()),
                ('terms_state', models.CharField(max_length=2)),
                ('terms_class', models.IntegerField()),
                ('terms_party', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
