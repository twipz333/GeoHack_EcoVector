# Generated by Django 3.2.9 on 2021-11-28 11:04

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20211128_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, null=True),
        ),
    ]