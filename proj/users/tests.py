from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class UsersTestCase(TestCase):
		def setUp(self):
			User = get_user_model()
			user = User.objects.create(
				email='example@example.com'
			)
			user.set_password('Uytrewq123')
			user.save()

		def test_register(self):
			data = {
				'email': 'example@example.com',
				'password': 'Uytrewq123'
			}
			res = self.client.post(reverse('register'), data=data)
			self.assertEqual(res.status_code, status.HTTP_201_CREATED)

		def test_login(self):
			data = {
				'email': 'example@example.com',
				'password': 'Uytrewq123'
			}
			res = self.client.post(reverse('login'), data=data)
			self.assertEqual(res.status_code, status.HTTP_200_OK)

		def test_jwt(self):
			data = {
				'email': 'example@example.com',
				'password': 'Uytrewq123'
			}
			res = self.client.post(reverse('login'), data=data)
			self.assertEqual(True, 'token' in res.json())