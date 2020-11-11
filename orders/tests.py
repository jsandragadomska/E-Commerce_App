from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class OrderTestCase(TestCase):

    def setUp(self):
        user_a = User.objects.create_user('user1', 'email1@email.com', 'user1password')
        user_a.is_staff = True
        user_a.is_superuser = False
        user_a.save()
        self.user_a = user_a
