from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from game_api.tests.test_sample import create_sample_topic, create_sample_game
from trivia_api.tests.test_samples import *
from trivia_api.models import Trivia, Question, Answer
from trivia_api.serializers import TriviaSerializer, TriviaQuestionSerializer, TriviaTopicDetailSerializer, \
    TriviaDetailSerializer

from game_api.models import Topic

TRIVIA_LIST_CREATE_URL = reverse('trivia_api:trivia')

def get_trivia_id_url(pk):
    return reverse('trivia_api:trivia', kwargs={'pk': pk})


def get_trivia_topic_id_url(pk):
    return reverse('trivia_api:trivia-topic', kwargs={'pk': pk})


class PublicTriviaAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_trivia_id_detail_auth_required(self):
        res = self.client.get(get_trivia_topic_id_url(1))
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_trivia_list_auth_required(self):
        res = self.client.get(TRIVIA_LIST_CREATE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_trivia_create_auth_required(self):
        res = self.client.post(TRIVIA_LIST_CREATE_URL, {})
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTrivaAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(email='test@example.com', password='test12345')
        self.client.force_authenticate(user=self.user)

    def test_list_trivia(self):
        topic = create_sample_topic(game=create_sample_game())
        create_sample_trivia(topic=topic, is_published=True)
        create_sample_trivia(topic=topic, is_published=True)
        create_sample_trivia(topic=topic, is_published=True)
        res = self.client.get(TRIVIA_LIST_CREATE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        trivias = Trivia.objects.filter(is_published=True).order_by('-id')
        serializer = TriviaQuestionSerializer(trivias, many=True)
        self.assertEqual(res.data, serializer.data)

    def test_list_trivia_only_published(self):
        topic = create_sample_topic(game=create_sample_game())
        create_sample_trivia(topic=topic, is_published=True)
        create_sample_trivia(topic=topic, is_published=True)
        create_sample_trivia(topic=topic, is_published=False)
        res = self.client.get(TRIVIA_LIST_CREATE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

    def test_list_trivia_all(self):
        topic = create_sample_topic(game=create_sample_game())
        create_sample_trivia(topic=topic, is_published=True)
        create_sample_trivia(topic=topic, is_published=True)
        create_sample_trivia(topic=topic, is_published=False)
        res = self.client.get(TRIVIA_LIST_CREATE_URL, {
            'all': True
        })
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 3)

    def test_create_simple_trivia(self):
        topic = create_sample_topic(game=create_sample_game())
        payload = {
            'topic': topic.pk,
            'is_published': True
        }
        res = self.client.post(TRIVIA_LIST_CREATE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        exists = Trivia.objects.filter(id=res.data['id']).exists()
        self.assertTrue(exists)

    def test_retrieve_trivia_id(self):
        topic = create_sample_topic(game=create_sample_game())
        trivia = create_sample_trivia(topic=topic, is_published=True)
        res = self.client.get(get_trivia_id_url(trivia.pk))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        serializer = TriviaDetailSerializer(trivia)
        self.assertEqual(res.data, serializer.data)

    def test_update_with_questions_trivia_id(self):
        topic = create_sample_topic(game=create_sample_game())
        trivia = create_sample_trivia(topic=topic, is_published=True)
        question1 = create_sample_question(question='my question 1', is_published=True)
        question2 = create_sample_question(question='my question 2', is_published=False)
        res = self.client.patch(get_trivia_id_url(trivia.pk), {
            'questions': [question1.pk, question2.pk]
        })
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        serializer = TriviaDetailSerializer(Trivia.objects.get(pk=trivia.pk))
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(res.data['questions'], serializer.data['questions'])
        self.assertEqual(len(res.data['questions']), len(serializer.data['questions']))

    def test_destroy_trivia_id(self):
        topic = create_sample_topic(game=create_sample_game())
        trivia = create_sample_trivia(topic=topic, is_published=True)
        res = self.client.delete(get_trivia_id_url(trivia.pk))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        exists = Trivia.objects.filter(id=trivia.pk).exists()
        self.assertFalse(exists)

    def test_retrieve_trivia_topic_details_id(self):
        topic = create_sample_topic(game=create_sample_game())
        create_sample_trivia(topic=topic, is_published=True)
        create_sample_trivia(topic=topic, is_published=True)
        create_sample_trivia(topic=topic, is_published=True)
        res = self.client.get(get_trivia_topic_id_url(topic.pk))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        serializer = TriviaTopicDetailSerializer(Topic.objects.get(pk=topic.pk))
        self.assertEqual(res.data, serializer.data)
