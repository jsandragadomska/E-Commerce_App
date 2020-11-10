from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Product

User = get_user_model()

class ProductTestCase(TestCase):

    def setUp(self):
        user_a = User.objects.create_user('user1', 'email1@email.com', 'user1password')
        user_a.is_staff = True
        user_a.is_superuser = False
        user_a.save()
        self.user_a = user_a
        user_b = User.objects.create_user('user2', 'email2@email.com', 'user2password')
        user_b.save()
        self.user_b = user_b

    def test_user_count(self):
        user_count = User.objects.all().count()
        print(user_count)
        self.assertEqual(user_count, 2)