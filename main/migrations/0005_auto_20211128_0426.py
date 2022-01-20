# Generated by Django 3.2.9 on 2021-11-28 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='tg_uid',
            field=models.CharField(blank=True, editable=False, max_length=9, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(editable=False, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='vk_uid',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True, unique=True),
        ),
    ]
