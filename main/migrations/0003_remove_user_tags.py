# Generated by Django 3.2.9 on 2021-11-27 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tags',
        ),
    ]
