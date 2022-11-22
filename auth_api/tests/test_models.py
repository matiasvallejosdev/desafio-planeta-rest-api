from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTest(TestCase):
    def test_create_user_with_email_successfully(self):
        email = 'test@example.com'
        password = 'test1954'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        email = 'TEST@example.com'
        user = get_user_model().objects.create_user(email=email, password='test1954')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        email = ''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=email)

    def test_create_superuser(self):
        email = 'test@example.com'
        password = 'test1954'
        user = get_user_model().objects.create_superuser(email=email, password=password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
