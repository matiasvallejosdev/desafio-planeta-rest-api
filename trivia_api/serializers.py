from rest_framework import serializers

from trivia_api.models import Answer, Question, Trivia
from game_api.models import Topic

from game_api.serializers import TopicBasicSerailizer


class TriviaAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer', 'is_correct',)


class TriviaQuestionSerializer(serializers.ModelSerializer):
    answers = TriviaAnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('question', 'type', 'answers', 'has_explication', 'explication',)
        read_only_fields = ('id',)
        depth = 1


class TriviaSerializer(serializers.ModelSerializer):
    # Serialize a foreigun key field
    # https://stackoverflow.com/questions/56298645/serializing-foreign-key-field
    # https://stackoverflow.com/questions/28309507/django-rest-framework-filtering-for-serializer-field
    questions = TriviaQuestionSerializer(many=True)

    class Meta:
        model = Trivia
        fields = ('id', 'questions',)
        read_only_fields = ('id',)
        depth = 2


class TopicTriviaSerializer(serializers.ModelSerializer):
    trivias = serializers.SerializerMethodField('get_trivias')

    def get_trivias(self, topic):
        return TriviaSerializer(Trivia.objects.filter(topic__id=topic.id, is_published=True), many=True).data

    class Meta:
        model = Topic
        fields = ('id', 'level', 'trivias', )
        read_only_fields = ('id', )
