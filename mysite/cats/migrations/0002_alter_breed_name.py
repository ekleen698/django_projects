# Generated by Django 4.2.7 on 2024-10-04 13:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='name',
            field=models.CharField(help_text='Enter an item', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Breed must be greater than 1 character')]),
        ),
    ]
