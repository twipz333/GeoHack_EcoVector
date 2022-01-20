# Generated by Django 3.2.9 on 2021-11-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_event_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='tag',
            new_name='tags',
        ),
        migrations.AddField(
            model_name='user',
            name='pref_channel',
            field=models.CharField(choices=[('tg', 'telegramm'), ('vk', 'vkontakte'), ('site', 'site'), ('na', 'not set')], default='na', max_length=4),
        ),
    ]
