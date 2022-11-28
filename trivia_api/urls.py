from django.urls import path, include
from rest_framework.routers import DefaultRouter

from trivia_api import views


app_name = 'trivia_api'
urlpatterns = [
    path('trivia/topic/<int:pk>/', views.TopicTriviaRetrieveAPI.as_view(), name='topic-trivia')
]
