from rest_framework import serializers
from game_api import models


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = ('id', 'name', 'summary', 'slot', 'pieces',)
        read_only_fields = ('id',)
        depth = 1


class GameBasicSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=240)
    subhead = serializers.CharField(max_length=240)


class TopicSerializer(serializers.ModelSerializer):
    game = GameBasicSerializer(read_only=True)

    class Meta:
        model = models.Topic
        fields = ('id', 'game', 'title', 'thumbnail', 'thumbnail_color', 'summary', 'featured',)
        read_only_fields = ('id',)
        depth = 1


class TopicBasicSerailizer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
