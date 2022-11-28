# Generated by Django 4.1 on 2022-11-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia_api', '0013_remove_question_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(blank=True, to='trivia_api.answer'),
        ),
    ]