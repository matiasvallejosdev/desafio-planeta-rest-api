from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from game_api import serializers
from game_api.models import Game, Topic


class GameAPI(viewsets.ModelViewSet):
    model = Game
    queryset = Game.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.GameSerializer


class TopicAPI(viewsets.ModelViewSet):
    model = Topic
    queryset = Topic.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TopicSerializer

    def get_queryset(self):
        return self.queryset.filter(is_published=True)
