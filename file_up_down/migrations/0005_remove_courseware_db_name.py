# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_up_down', '0004_auto_20180105_0327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseware_db',
            name='name',
        ),
    ]
