from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from trivia_api.serializers import TriviaSerializer, TriviaQuestionSerializer, TriviaTopicDetailSerializer, TriviaDetailSerializer
from trivia_api.models import Trivia, Question
from game_api.models import Topic


class TriviaListCreateView(generics.ListCreateAPIView):
    queryset = Trivia.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TriviaSerializer

    def get_queryset(self):
        is_all = self.request.query_params.get('all')
        return self.queryset.order_by('-id') if is_all else self.queryset.filter(is_published=True).order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.serializer_class
        return TriviaQuestionSerializer


class TriviaTopicRetrieveView(generics.RetrieveAPIView):
    queryset = Topic.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TriviaTopicDetailSerializer

    def get(self, request, pk=None, **kwargs):
        is_all = self.request.query_params.get('all')
        topic = self.get_object(pk=pk)
        serializer = self.serializer_class(topic, context={
            'all': is_all
        }, many=False)
        return Response(serializer.data)

    def get_object(self, pk=None):
        is_all = self.request.query_params.get('all')
        return get_object_or_404(Topic, pk=pk) if is_all else get_object_or_404(Topic, pk=pk, is_published=True)


class TriviaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trivia.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TriviaDetailSerializer
