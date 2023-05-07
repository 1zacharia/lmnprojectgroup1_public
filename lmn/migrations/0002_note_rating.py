# Generated by Django 3.1.2 on 2023-04-30 16:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='rating',
            field=models.IntegerField(blank=True, default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]
