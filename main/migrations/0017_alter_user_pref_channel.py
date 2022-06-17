# Generated by Django 3.2.9 on 2021-11-28 11:14

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pref_channel',
            field=models.CharField(choices=[('tg', 'telegramm'), ('vk', 'vkontakte'), ('site', 'site'), ('na', 'not set')], default=False, max_length=4, null=True),
        ),
    ]