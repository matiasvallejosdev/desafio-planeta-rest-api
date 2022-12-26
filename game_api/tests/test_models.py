from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model

from game_api.models import Game, Topic, Piece, Slot

from PIL import Image


def create_sample_image(width=400, height=300):
    return Image.new(mode="RGB", size=(width, height))


class ModelTestCase(TestCase):
    def test_slot_str(self):
        slot = Slot.objects.create(
            name='Slot model',
            image=None
        )
        self.assertIn(slot.name, str(slot))

    def test_piece_str(self):
        piece = Piece.objects.create(
            name='Piece model',
            image=None
        )
        self.assertIn(piece.name, str(piece))

    def test_game_str(self):
        game = Game.objects.create(
            name='My name',
            subhead='Subhead',
            summary='',
            color='green',
            slot=Slot.objects.create(name='Slot'),
            is_published=True,
        )
        game.pieces.add(Piece.objects.create(name='Piece'))
        self.assertIn(game.name, str(game))

    def test_topic_str(self):
        game = Game.objects.create(
            name='My name',
            subhead='Subhead',
            summary='',
            color='green',
            slot=Slot.objects.create(name='Slot'),
            is_published=True
        )
        topic = Topic.objects.create(
            level='easy',
            game=game,
            title='Title',
            summary='',
            thumbnail=None,
            featured=False,
            is_published=True,
            created_at=timezone.now()
        )
        self.assertIn(topic.title, str(topic))
