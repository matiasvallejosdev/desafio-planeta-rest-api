from django.urls import path, include
from rest_framework.routers import DefaultRouter

from game_api import views
router = DefaultRouter()
router.register('game', views.GameAPI)
router.register('topic', views.TopicAPI)

app_label = 'game_api'
urlpatterns = [
    path('', include(router.urls))
]
