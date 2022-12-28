from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

from game_api.models import Game, Topic, Slot, Piece
from game_api.serializers import GameSerializer, GameTopicsDetailSerializer, GamePiecesDetailSerializer

from .test_sample import *

import json

GAME_LIST_CREATE_URL = reverse('game_api:game')


def get_game_id_url(pk):
    """GAME_RETRIEVE_UPDATE_DESTROY_URL"""
    return reverse('game_api:game', kwargs={'pk': pk})


class PublicGameAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_required_auth(self):
        res = self.client.get(GAME_LIST_CREATE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_required_auth(self):
        res = self.client.post(GAME_LIST_CREATE_URL, {})
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_required_auth(self):
        res = self.client.post(get_game_id_url(1))
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateGameAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create(email='email@example.com', password='password')
        self.client.force_authenticate(user=self.user)

    def test_list_game(self):
        game = create_sample_game()
        create_sample_topic(title='topic1', game=game)
        create_sample_topic(title='topic2', game=game)
        res = self.client.get(GAME_LIST_CREATE_URL)
        games = Game.objects.all().filter(is_published=True).order_by('id')
        serializer = GameTopicsDetailSerializer(games, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_list_game_only_published(self):
        game1 = create_sample_game(is_published=True)
        game2 = create_sample_game(is_published=False)
        game3 = create_sample_game(is_published=False)
        create_sample_topic(title='topic1_published', game=game1, is_published=True)
        create_sample_topic(title='topic2_published', game=game1, is_published=True)
        create_sample_topic(title='topic3_published', game=game2, is_published=True)
        create_sample_topic(title='topic4', game=game2, is_published=False)
        create_sample_topic(title='topic5', game=game3, is_published=False)
        create_sample_topic(title='topic6', game=game3, is_published=False)
        res = self.client.get(GAME_LIST_CREATE_URL)
        self.assertEqual(len(res.data), 1)

    def test_list_game_all(self):
        game1 = create_sample_game(name='game1', is_published=True)
        game2 = create_sample_game(name='game2', is_published=False)
        create_sample_topic(title='topic1', game=game1, is_published=True)
        create_sample_topic(title='topic2', game=game1, is_published=True)
        create_sample_topic(title='topic3', game=game2, is_published=False)
        res = self.client.get(GAME_LIST_CREATE_URL, {'all': True})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(len(res.data) == 2)

    def test_list_topic_all(self):
        game1 = create_sample_game(name='game1', is_published=True)
        game2 = create_sample_game(name='game2', is_published=False)
        create_sample_topic(title='topic1', game=game1, is_published=True)
        create_sample_topic(title='topic2', game=game1, is_published=True)
        create_sample_topic(title='topic3', game=game1, is_published=False)
        create_sample_topic(title='topic4', game=game2, is_published=False)
        create_sample_topic(title='topic5', game=game2, is_published=True)
        res = self.client.get(GAME_LIST_CREATE_URL, {'all': True})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(len(res.data) == 2)
        self.assertEqual(len(res.data[0]['topics']), 2)
        self.assertEqual(len(res.data[1]['topics']), 3)

    def test_create_basic_game(self):
        payload = {
            'name': 'New game',
            'subhead': 'This is my new game',
            'slot': Slot.objects.create(name='Slot').id,
            'is_published': True
        }
        res = self.client.post(GAME_LIST_CREATE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        game = Game.objects.filter(id=res.data['id']).exists()
        self.assertTrue(game)

    def test_create_game_with_pieces(self):
        piece1 = Piece.objects.create(name='Piece1')
        piece2 = Piece.objects.create(name='Piece2')
        payload = {
            'name': 'New game',
            'subhead': 'This is my new game',
            'slot': Slot.objects.create(name='Slot').id,
            'pieces': [piece1.id, piece2.id],
            'is_published': True
        }
        res = self.client.post(GAME_LIST_CREATE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        game = Game.objects.get()
        pieces = game.pieces.all()
        self.assertEqual(pieces.count(), 2)
        self.assertIn(piece1, pieces)
        self.assertIn(piece2, pieces)

    def test_retrieve_details_game_id(self):
        game = create_sample_game()
        res = self.client.get(get_game_id_url(game.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        serializer = GamePiecesDetailSerializer(game)
        self.assertEqual(res.data, serializer.data)
