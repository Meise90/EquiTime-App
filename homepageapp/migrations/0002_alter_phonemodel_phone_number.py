# Generated by Django 4.1.7 on 2023-08-04 11:13

import django.core.validators
from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('homepageapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, validators=[django.core.validators.RegexValidator(message="Phone number format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
