from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from trivia_api import serializers
from trivia_api.models import Trivia, Question


class TriviaAPI(viewsets.ModelViewSet):
    model = Trivia
    queryset = Trivia.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TriviaSerializer
    # It was setting up by default
    # filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('topic__id',)

    def get_queryset(self):
        return self.queryset.filter(is_published=True)


class QuestionAPI(viewsets.ModelViewSet):
    model = Question
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.QuestionSerializer
