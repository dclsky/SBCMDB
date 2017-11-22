# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('system', models.CharField(max_length=32, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('ip', models.CharField(max_length=32)),
                ('mac', models.CharField(max_length=32)),
                ('controler', models.CharField(max_length=32, verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98')),
                ('statue', models.CharField(max_length=8, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
            ],
        ),
    ]
