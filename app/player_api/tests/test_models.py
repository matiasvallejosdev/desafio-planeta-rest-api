from django.contrib.auth import get_user_model
from django.test import TestCase
from player_api.models import Player

class ModelTests(TestCase):
    """Test models"""
    def test_create_player_with_user(self):
        """Test creating a new player with an user."""
        email = 'vallejostmati@email.com'
        password = 'test12345'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        player = Player.objects.get(user=user)
        self.assertIsNotNone(player)
        self.assertEqual(user.email, email)
