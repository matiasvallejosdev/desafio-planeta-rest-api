from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from trivia_api import serializers
from trivia_api.models import Trivia, Question
from game_api.models import Topic


class TopicTriviaRetrieveAPI(generics.RetrieveAPIView):
    queryset = Topic.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TopicTriviaSerializer

    def get_queryset(self):
        return self.queryset.filter(is_published=True)
