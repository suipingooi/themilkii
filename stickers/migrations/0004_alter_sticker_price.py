# Generated by Django 3.2.3 on 2021-06-15 11:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickers', '0003_alter_sticker_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sticker',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
