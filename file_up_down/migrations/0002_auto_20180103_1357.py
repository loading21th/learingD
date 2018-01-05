# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_up_down', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseware_db',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('content', models.FileField(upload_to=b'./upoloadfile/')),
            ],
        ),
        migrations.DeleteModel(
            name='coursefile_db',
        ),
    ]
