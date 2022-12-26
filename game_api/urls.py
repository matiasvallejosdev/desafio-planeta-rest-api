from django.urls import path, include
from game_api.views import GameListCreateView, GameRetrieveUpdateDestroyView, TopicListCreateView, TopicRetrieveUpdateDestroyView

app_name = 'game_api'
urlpatterns = [
    path('game/', GameListCreateView.as_view(), name='game'),
    path('game/<int:pk>/', GameRetrieveUpdateDestroyView.as_view(), name='game'),
    path('topic/', TopicListCreateView.as_view(), name='topic'),
    path('topic/<int:pk>/', TopicRetrieveUpdateDestroyView.as_view(), name='topic'),
]
