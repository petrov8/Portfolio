# Generated by Django 4.1.7 on 2023-02-26 12:49

import django.core.validators
from django.db import migrations, models
import support.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='message',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10, message='Must be at least 10 chars long.')], verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='number',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(10, message='Must be at least 10 digits long.'), django.core.validators.MaxLengthValidator(16, message='Must be no more than 16 chars long.'), support.validators.check_if_digits_only], verbose_name='Contact Number'),
        ),
    ]
