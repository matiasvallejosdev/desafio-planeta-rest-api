from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTest(TestCase):
    def create_user_with_email_successfully(self):
        email = 'test@example.com'
        password = 'test1954'
        user = get_user_model().create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
