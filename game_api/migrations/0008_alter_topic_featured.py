# Generated by Django 4.1 on 2022-11-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_api', '0007_alter_game_pieces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='featured',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
