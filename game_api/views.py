from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from game_api import serializers
from game_api.models import Game, Topic


class TopicListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.TopicSerializer
    queryset = Topic.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        is_all = self.request.query_params.get('all')
        return self.queryset.order_by('-id') if is_all is not None else self.queryset.filter(is_published=True).order_by('id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.TopicPostSerializer
        return self.serializer_class


class TopicRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TopicSerializer
    queryset = Topic.objects.all()
    permission_classes = (IsAuthenticated,)


class GameListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.GameTopicsDetailSerializer
    queryset = Game.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        is_all = self.request.query_params.get('all')
        return self.queryset.order_by('-id') if is_all is not None \
            else self.queryset.filter(is_published=True).order_by('-id')

    def get(self, request, **kwargs):
        is_all = self.request.query_params.get('all')
        games = self.get_queryset()
        serializer = self.serializer_class(games, context={
            'all': is_all
        }, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.GamePostSerializer
        return self.serializer_class


class GameRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.GamePiecesDetailSerializer
