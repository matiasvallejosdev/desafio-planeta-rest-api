# Generated by Django 4.0 on 2023-07-18 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=240)),
                ('subhead', models.CharField(blank=True, max_length=45)),
                ('summary', models.CharField(blank=True, max_length=240)),
                ('color', models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE')], default='green', max_length=6)),
                ('is_published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=240)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=240)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('easy', 'EASY'), ('medium', 'MEDIUM'), ('hard', 'HARD')], default='easy', max_length=12)),
                ('title', models.CharField(max_length=75)),
                ('summary', models.CharField(blank=True, max_length=150)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('featured', models.BooleanField(blank=True, default=False)),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game_api.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='pieces',
            field=models.ManyToManyField(blank=True, to='game_api.Piece'),
        ),
        migrations.AddField(
            model_name='game',
            name='slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='game_api.slot'),
        ),
    ]
