from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import CustomUser

class RegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('api:register')
        self.valid_payload = {
            'name': 'Bijay Khadka',
            'email': 'bijay@example.com',
            'phone_number': '1234567890',
            'password': 'pa$$word',
        }

    def test_registration_success(self):
        response = self.client.post(self.register_url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().name, 'Bijay Khadka')

    def test_registration_failure(self):
        # Test case for invalid payload or missing data
        invalid_payload = {
            'name': 'Bijay Khadka',
            'email': 'invalidemail',  # Invalid email format
            'password': 'pa$$word',
        }
        response = self.client.post(self.register_url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class LoginLogoutTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('api:register')
        self.login_url = reverse('api:login')
        self.logout_url = reverse('api:logout')
        self.valid_payload = {
            'name': 'Bijay Khadka',
            'email': 'bijay@example.com',
            'phone_number': '1234567890',
            'password': 'pa$$word',
        }

    def test_login_success(self):
        # Register the user first
        self.client.post(self.register_url, self.valid_payload, format='json')

        # Now, test login
        login_data = {'email': 'bijay@example.com', 'password': 'pa$$word'}
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_logout_success(self):
        # Register the user first
        self.client.post(self.register_url, self.valid_payload, format='json')

        # Login the user
        login_data = {'email': 'bijay@example.com', 'password': 'pa$$word'}
        self.client.post(self.login_url, login_data, format='json')

        # Now, test logout
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], 'User successfully logged out.')
