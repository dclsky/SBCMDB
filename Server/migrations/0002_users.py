# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xa7\x93\xe5\x90\x8d')),
                ('password', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xaf\x86\xe7\xa0\x81')),
                ('phone', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\x94\xb5\xe8\xaf\x9d')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe9\x82\xae\xe7\xae\xb1', blank=True)),
                ('photo', models.ImageField(upload_to=b'img')),
            ],
        ),
    ]
