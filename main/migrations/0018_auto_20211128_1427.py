# Generated by Django 3.2.9 on 2021-11-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_user_pref_channel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='pref_channel',
            field=models.CharField(choices=[('tg', 'telegramm'), ('vk', 'vkontakte'), ('site', 'site'), ('na', 'not set')], default=False, max_length=4),
        ),
    ]