from django.test import TestCase😂
from .models import CustomUser

class CustomUserTest(TestCase):
    def test_create_user(self):
        """
        Test that a user can be created with an email and password.
        """
        user = CustomUser.objects.create_user(email='test@example.com', password='testpass123')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpass123'))
