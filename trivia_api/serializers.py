from rest_framework import serializers
from trivia_api import models

from game_api.serializers import TopicBasicSerailizer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = ('id', 'answer', 'is_correct',)
        read_only_fields = ('id',)


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = models.Question
        fields = ('id', 'question', 'type', 'answers', 'has_explication', 'explication',)
        read_only_fields = ('id',)
        depth = 1


class TriviaSerializer(serializers.ModelSerializer):
    topic = TopicBasicSerailizer()
    # Serialize a foreigun key field
    # https://stackoverflow.com/questions/56298645/serializing-foreign-key-field
    # https://stackoverflow.com/questions/28309507/django-rest-framework-filtering-for-serializer-field
    questions = QuestionSerializer(many=True)

    class Meta:
        model = models.Trivia
        fields = ('id', 'topic', 'questions',)
        read_only_fields = ('id',)
        depth = 2
