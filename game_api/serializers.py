from rest_framework import serializers
from game_api.models import Topic, Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'color', 'slot', 'pieces',)
        read_only_fields = ('id',)
        depth = 1


class GameBasicSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=240)
    subhead = serializers.CharField(max_length=240)


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'title', 'thumbnail', 'summary', 'featured',)
        read_only_fields = ('id',)
        depth = 1


class GameTopicSerializer(serializers.ModelSerializer):
    topics = serializers.SerializerMethodField('get_topics')

    def get_topics(self, game):
        return TopicSerializer(Topic.objects.filter(game__id=game.id, is_published=True), many=True).data

    class Meta:
        model = Game
        fields = ('id', 'name', 'summary', 'subhead', 'color', 'topics')
        read_only_fields = ('id', 'topics', )
        depth = 1


class TopicBasicSerailizer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
