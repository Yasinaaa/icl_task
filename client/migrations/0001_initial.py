# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import client.models
import client.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientFileModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=256)),
                ('path_to_file', models.FileField(blank=True, upload_to=client.models.get_path, validators=[client.validators.validate_file_extension])),
            ],
            options={
                'db_table': 'graphs_table',
            },
        ),
    ]
