# Generated by Django 3.2.9 on 2021-11-27 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique_for_date='date')),
                ('description', models.TextField(max_length=250)),
                ('date', models.DateTimeField(verbose_name='date of event')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(editable=False, max_length=20, unique=True)),
                ('tags', models.CharField(default='{}', max_length=1000)),
                ('tg_uid', models.CharField(editable=False, max_length=9, null=True, unique=True)),
                ('vk_uid', models.CharField(editable=False, max_length=20, null=True, unique=True)),
                ('username', models.CharField(max_length=15, null=True, unique=True)),
                ('password', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
