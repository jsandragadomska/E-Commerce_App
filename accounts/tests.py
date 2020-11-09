from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()
# Create your tests here.
class UserTestCast(TestCase):
    def setUp(self):
        user_a = User(username='cfe', email='email@email.com')
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password('cfepassword')
        user_a.save()
        print(user_a.id)

    def tests_user_exists(self):
        user_count = User.objects.all().count()
        print(user_count)
        self.assertEqual(user_count, 1)