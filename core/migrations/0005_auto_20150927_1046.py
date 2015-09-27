# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='ratub',
            new_name='rating',
        ),
    ]
