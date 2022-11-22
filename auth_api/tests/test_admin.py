from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='testadmin@example.com',
            password='testpassword'
        )
        self.client.force_login(self.admin_user)
        self.standard_user = get_user_model().objects.create_user(
            email='teststandard@example.com',
            password='testpassword',
            instance_name='testing'
        )
