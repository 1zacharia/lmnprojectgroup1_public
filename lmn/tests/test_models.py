from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError


class TestUser(TestCase):

    def test_create_user_duplicate_username_fails(self):
        user = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        user.save()

        user2 = User(username='bob', email='another_bob@bob.com', first_name='bob', last_name='bob')
        with self.assertRaises(IntegrityError):
            user2.save()

    def test_create_user_duplicate_email_fails(self):
        user = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        user.save()

        user2 = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        with self.assertRaises(IntegrityError):
            user2.save()


# class TestNote(TestCase):

    # fixtures for users, artists, venues, and shows to test note
    
    # Test rating below minimum invalid

    # Test rating above maximum invalid

    # Test valid rating