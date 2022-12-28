from rest_framework import serializers
from game_api.models import Topic, Game, Slot, Piece

# Using depth in serializers
# https://medium.com/@rudmanmrrod/django-rest-framework-uso-del-depth-en-serializer-a500969779e9
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name',)
        read_only_fields = ('id',)
        depth = 1


class GamePostSerializer(serializers.ModelSerializer):
    slot = serializers.PrimaryKeyRelatedField(many=False, queryset=Slot.objects.all(), required=False)
    pieces = serializers.PrimaryKeyRelatedField(many=True, queryset=Piece.objects.all(), required=False)

    class Meta:
        model = Game
        fields = ('id', 'name', 'color', 'slot', 'pieces',)
        read_only_fields = ('id',)
        depth = 1


class GamePiecesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'color', 'slot', 'pieces',)
        read_only_fields = ('id',)
        depth = 2


class GameTopicsDetailSerializer(serializers.ModelSerializer):
    topics = serializers.SerializerMethodField('get_topics')

    def _is_all(self):
        is_all = self.context.get('all', False)
        if is_all:
            return True
        return False

    def get_topics(self, game):
        if self._is_all():
            return TopicSerializer(Topic.objects.filter(game__id=game.id), many=True).data
        else:
            return TopicSerializer(Topic.objects.filter(game__id=game.id, is_published=True), many=True).data

    class Meta:
        model = Game
        fields = ('id', 'name', 'summary', 'subhead', 'color', 'topics', )
        read_only_fields = ('id', 'topics',)
        depth = 1


class TopicSerializer(serializers.ModelSerializer):
    game = GameSerializer()

    class Meta:
        model = Topic
        fields = ('id', 'title', 'thumbnail', 'summary', 'featured', 'level', 'game', 'is_published', )
        read_only_fields = ('id',)
        depth = 1


class TopicPostSerializer(serializers.ModelSerializer):
    game = serializers.PrimaryKeyRelatedField(many=False, queryset=Game.objects.all(), required=False)

    class Meta:
        model = Topic
        fields = ('id', 'title', 'thumbnail', 'summary', 'featured', 'level', 'game', 'is_published', )
        read_only_fields = ('id',)
