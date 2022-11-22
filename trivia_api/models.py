from django.db import models
from game_api.models import Topic


# Create your models here.

class Trivia(models.Model):
    title = models.CharField(max_length=255, null=True)
    topic = models.ForeignKey(Topic, null=True, blank=True, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Type(models.Model):
    name = models.CharField(max_length=255)


class Question(models.Model):
    question = models.CharField(max_length=255, null=True)
    type = models.ForeignKey(Type, blank=True, null=True, on_delete=models.SET_NULL)
    trivia = models.ForeignKey(Trivia, blank=True, null=True, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Answer(models.Model):
    answer = models.CharField(max_length=255, blank=True, null=True)
    is_correct = models.BooleanField(default=False)
