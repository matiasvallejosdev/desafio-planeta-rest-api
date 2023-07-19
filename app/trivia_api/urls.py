from django.urls import path, include
from rest_framework.routers import DefaultRouter

from trivia_api.views import TriviaListCreateView, TriviaTopicRetrieveView, TriviaRetrieveUpdateDestroyView


app_name = 'trivia_api'
urlpatterns = [
    path('trivia/', TriviaListCreateView.as_view(), name='trivia'),
    path('trivia/<int:pk>/', TriviaRetrieveUpdateDestroyView.as_view(), name='trivia'),
    path('trivia/topic/<int:pk>/', TriviaTopicRetrieveView.as_view(), name='trivia-topic')
]
