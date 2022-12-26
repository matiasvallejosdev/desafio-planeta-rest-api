from rest_framework import serializers
from game_api.models import Topic, Game, Slot, Piece


class GameSerializer(serializers.ModelSerializer):
    slot = serializers.PrimaryKeyRelatedField(many=False, queryset=Slot.objects.all(), required=False)
    pieces = serializers.PrimaryKeyRelatedField(many=True, queryset=Piece.objects.all(), required=False)

    class Meta:
        model = Game
        fields = ('id', 'name', 'color', 'slot', 'pieces',)
        read_only_fields = ('id',)
        depth = 1


class GameDetailSerializer(serializers.ModelSerializer):
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
        fields = ('id', 'name', 'summary', 'subhead', 'color', 'topics')
        read_only_fields = ('id', 'topics',)
        depth = 1


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'title', 'thumbnail', 'summary', 'featured', 'level',)
        read_only_fields = ('id',)
        depth = 1

# class GameBasicSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=240)
#     subhead = serializers.CharField(max_length=240)

# class TopicBasicSerailizer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
