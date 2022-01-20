# Generated by Django 3.2.9 on 2021-11-28 11:03

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20211128_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='verified',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pref_channel',
            field=models.CharField(choices=[('tg', 'telegramm'), ('vk', 'vkontakte'), ('site', 'site'), ('na', 'not set')], default=False, max_length=4),
        ),
    ]
