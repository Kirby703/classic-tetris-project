# Generated by Django 2.2.2 on 2019-06-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classic_tetris_project', '0002_auto_20190628_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discorduser',
            name='discord_id',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='twitchuser',
            name='twitch_id',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
