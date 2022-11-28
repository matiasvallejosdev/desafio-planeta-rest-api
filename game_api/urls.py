from django.urls import path, include
from game_api import views

app_name = 'game_api'
urlpatterns = [
    path('game/<int:pk>/', views.GameRetrieveAPI.as_view(), name='game-pk'),
    path('topic/<int:pk>/', views.TopicRetrieveAPI.as_view(), name='topic-pk'),
    path('topics/', views.TopicListAPI.as_view(), name='topic-list4')
]
