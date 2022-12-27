from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from game_api.models import Game, Topic, Slot, Piece
from game_api.serializers import TopicSerializer

from .test_sample import *

TOPIC_LIST_CREATE_URL = reverse('game_api:topic')


def get_topic_id_url(pk):
    return reverse('game_api:topic', kwargs={'pk': pk})


class PublicTopicAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_require_auth(self):
        res = self.client.get(TOPIC_LIST_CREATE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_require_auth(self):
        res = self.client.get(get_topic_id_url(1))
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTopicAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create(email='user@example.com', password='195321')
        self.client.force_authenticate(user=self.user)

    def test_list_topic(self):
        game = create_sample_game()
        create_sample_topic(title='topic1', game=game)
        create_sample_topic(title='topic2', game=game)
        res = self.client.get(TOPIC_LIST_CREATE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        topics = Topic.objects.filter(is_published=True).order_by('-id')
        serializer = TopicSerializer(topics, many=True)
        self.assertEqual(res.data, serializer.data)

    def test_list_topic_only_published(self):
        game = create_sample_game()
        create_sample_topic(title='topic1', game=game, is_published=True)
        create_sample_topic(title='topic2', game=game, is_published=True)
        create_sample_topic(title='topic3', game=game, is_published=False)
        res = self.client.get(TOPIC_LIST_CREATE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(len(res.data) == 2)

    def test_list_topic_all(self):
        game1 = create_sample_game(name='game1', is_published=True)
        create_sample_topic(title='topic1', game=game1, is_published=True)
        create_sample_topic(title='topic2', game=game1, is_published=True)
        create_sample_topic(title='topic3', game=game1, is_published=False)
        res = self.client.get(TOPIC_LIST_CREATE_URL, {'all': True})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(len(res.data) == 3)

    def test_create_simple_topic(self):
        game1 = create_sample_game(name='game1', is_published=True)
        payload = {
            'title': 'Topic1',
            'game': game1.pk,
            'is_published': True,
        }
        res = self.client.post(TOPIC_LIST_CREATE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        exists = Topic.objects.filter(id=res.data['id']).exists()
        self.assertTrue(exists, True)

    def test_retrieve_details_topic_id(self):
        topic = create_sample_topic()
        res = self.client.get(get_topic_id_url(topic.pk))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        serializer = TopicSerializer(topic)
        self.assertEqual(res.data, serializer.data)

    def test_update_details_topic_id(self):
        topic = create_sample_topic(title='Title')
        res = self.client.patch(get_topic_id_url(topic.pk), {
            'title': 'My new title'
        })
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        serializer = TopicSerializer(Topic.objects.get(pk=topic.pk))
        self.assertEqual(serializer.data, res.data)

    def test_destroy_details_topic_id(self):
        topic = create_sample_topic()
        res = self.client.delete(get_topic_id_url(topic.pk))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        exists = Topic.objects.filter(id=topic.pk).exists()
        self.assertFalse(exists)
