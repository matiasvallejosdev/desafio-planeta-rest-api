from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated

from game_api import serializers
from game_api.models import Game, Topic


class GameRetrieveAPI(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.GameSerializer


class TopicRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = serializers.TopicSerializer
    queryset = Topic.objects.all()
    permission_classes = (IsAuthenticated,)


class TopicListAPI(generics.ListAPIView):
    serializer_class = serializers.GameTopicSerializer
    queryset = Game.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(is_published=True).order_by('id')
