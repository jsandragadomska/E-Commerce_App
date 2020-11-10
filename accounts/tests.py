from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()
# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        user_a = User(username='cfe', email='email@email.com')
        user_a_pw = 'cfepassword'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.save()
        user_a.set_password(user_a_pw)
        self.user_a = user_a

    def test_user_exists(self):
        user_count = User.objects.all().count()
        print(user_count)
        self.assertEqual(user_count, 1)

    def test_user_password(self):
        self.assertTrue(self.user_a.check_password(self.user_a_pw))

# Need to solve the problem. 
#   def test_login_url(self):
#        login_url = settings.LOGIN_URL
#        data = {'username': 'cfe', 'password': self.user_a_pw}
#        response = self.client.post(login_url, data, follow=True)
#        status_code = response.status_code
#        redirect_path = response.request.get("PATH_INFO")
#        self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
#        self.assertEqual(status_code, 200)

