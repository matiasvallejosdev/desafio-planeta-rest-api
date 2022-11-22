from rest_framework import serializers
from game_api import models


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = ('id', 'name', 'slot', 'pieces',)
        read_only_fields = ('id',)
        depth = 1


class GameBasicSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class TopicSerializer(serializers.ModelSerializer):
    game = GameBasicSerializer(read_only=True)

    class Meta:
        model = models.Topic
        fields = ('id', 'game', 'title', 'thumbnail', 'thumbnail_color', 'summary', 'featured',)
        read_only_fields = ('id',)
        depth = 1
