from django.test import TestCase
from django.contrib.auth.models import User

class UserAuthTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_login(self):
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login successful')

    def test_register(self):
        response = self.client.post('/register/', {
            'username': 'newuser',
            'password1': 'password123',
            'password2': 'password123',
            'email': 'newuser@example.com'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='newuser').exists())
