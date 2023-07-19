from django.db import models
from game_api.models import Topic


class Answer(models.Model):
    answer = models.CharField(max_length=255, blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        state = '✅' if self.is_correct else '❌'
        return f"{state} {self.answer}"


class Question(models.Model):
    TYPE_CHOICES = (
        ('TwoAnswers', 'TwoAnswers'),
        ('FourAnswers', 'FourAnswers')
    )
    question = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, default='FourAnswers')
    answers = models.ManyToManyField(Answer, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        published = '👍' if self.is_published else '👎'
        return f"{published} → {self.question}"


class Trivia(models.Model):
    trivia_name = models.CharField(max_length=255, null=True)
    trivia_paragraph = models.TextField(blank=True, null=True)
    topic = models.ForeignKey(Topic, null=True, blank=True, on_delete=models.SET_NULL)
    questions = models.ManyToManyField(Question, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        published = '👍' if self.is_published else '👎'
        return f"{published} → Trivia {self.pk} → {self.trivia_name} → {self.topic.title}"
