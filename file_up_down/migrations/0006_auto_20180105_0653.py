# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_up_down', '0005_remove_courseware_db_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseware_db',
            name='content',
            field=models.FileField(upload_to=b'uploadfile/'),
        ),
    ]
