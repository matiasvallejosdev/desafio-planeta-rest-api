from rest_framework import serializers

from trivia_api.models import Answer, Question, Trivia

from game_api.models import Topic
from game_api.serializers import TopicSerializer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer', 'is_correct',)


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('question', 'type', 'answers',)
        read_only_fields = ('id',)
        depth = 1


class TriviaQuestionSerializer(serializers.ModelSerializer):
    # Serialize a foreigun key field
    # https://stackoverflow.com/questions/56298645/serializing-foreign-key-field
    # https://stackoverflow.com/questions/28309507/django-rest-framework-filtering-for-serializer-field
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Trivia
        fields = ('id', 'questions',)
        read_only_fields = ('id',)
        depth = 2


class TriviaTopicDetailSerializer(serializers.ModelSerializer):
    trivias = serializers.SerializerMethodField('get_trivias')

    def _is_all(self):
        is_all = self.context.get('all', False)
        if is_all:
            return True
        return False

    def get_trivias(self, topic):
        if self._is_all():
            return TriviaQuestionSerializer(Trivia.objects.filter(topic__id=topic.id), many=True).data
        else:
            return TriviaQuestionSerializer(Trivia.objects.filter(topic__id=topic.id, is_published=True),
                                            many=True).data

    class Meta:
        model = Topic
        fields = ('id', 'level', 'trivias',)
        read_only_fields = ('id',)


class TriviaDetailSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(many=False)
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Trivia
        fields = ('id', 'topic', 'questions', 'is_published', 'created_at',)
        read_only_fields = ('id', 'created_at',)
        depth = 1


class TriviaSerializer(serializers.ModelSerializer):
    topic = serializers.PrimaryKeyRelatedField(many=False, queryset=Topic.objects.all(), required=False)
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all(), required=False)

    class Meta:
        model = Trivia
        fields = ('id', 'topic', 'questions', 'is_published', 'created_at',)
        read_only_fields = ('id', 'created_at',)
        depth = 1
