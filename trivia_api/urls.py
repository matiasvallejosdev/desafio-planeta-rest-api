from django.urls import path, include
from rest_framework.routers import DefaultRouter

from trivia_api import views

router = DefaultRouter()
router.register('trivia', views.TriviaAPI, basename='trivia')
router.register('question', views.QuestionAPI, basename='question')

app_name = 'trivia_api'
urlpatterns = [
    path('', include(router.urls))
]
