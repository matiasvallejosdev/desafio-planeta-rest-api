from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CONNECTION_URL = reverse('auth_api:connection-verify')

def create_user(**kwargs):
    return get_user_model().objects.create_user(**kwargs)


class PublicUserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    
class PrivateUserAPITest(TestCase):
    def setUp(self):
        self.user = create_user(email='test@example.com', password='test12345')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_connecion(self):
        res = self.client.post(CONNECTION_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            "detail": "Connection successfully!"
        })

