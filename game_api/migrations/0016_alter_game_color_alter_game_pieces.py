# Generated by Django 4.0 on 2022-12-14 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_api', '0015_alter_topic_summary_alter_topic_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='color',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE')], default='black', max_length=6),
        ),
        migrations.AlterField(
            model_name='game',
            name='pieces',
            field=models.ManyToManyField(blank=True, to='game_api.Piece'),
        ),
    ]
