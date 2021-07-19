from .models import Note, Todo
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class NotesTestCase(TestCase):
		def setUp(self):
				User = get_user_model()

				# Creating user
				user = User.objects.create(
					email='example@example.com'
				)
				user.set_password('Uytrewq123')
				user.save()

				# Creating note
				note = Note.objects.create(
					text='First note',
					author=user
				)

				#Creating Todo
				todo = Todo.objects.create(
					text='First todo',
					author=user
				)

		def test_list_note(self):
				token = self.client.post(
					reverse('login'),
					data={
						'email': 'example@example.com',
						'password': 'Uytrewq123'
					}
				).json()['token']
				res = self.client.get(
					reverse('list_create_note'),
					headers={
						'Authorization': f'JWT {token}'
					}
				)
				self.assertEqual(res.status_code, status.HTTP_200_OK)

		def test_create_note(self):
				token = self.client.post(
					reverse('login'),
					data={
						'email': 'example@example.com',
						'password': 'Uytrewq123'
					}
				).json()['token']
				res = self.client.post(
					reverse('list_create_note'),
					data = {
						'text': 'Second post'
					},
					headers={
						'Authorization': f'JWT {token}'
					}
				)
				self.assertEqual(res.status_code, status.HTTP_201_CREATED)

		def test_retrieve_note(self):
				token = self.client.post(
					reverse('login'),
					data={
						'email': 'example@example.com',
						'password': 'Uytrewq123'
					}
				).json()['token']
				res = self.client.get(
					reverse('get_update_delete_note', kwargs={'pk': 1}),
					headers={
						'Authorization': f'JWT {token}'
					}
				)
				self.assertEqual(res.status_code, status.HTTP_200_OK)

		def test_update_note(self):
				token = self.client.post(
					reverse('login'),
					data={
						'email': 'example@example.com',
						'password': 'Uytrewq123'
					}
				).json()['token']
				res = self.client.put(
					reverse('get_update_delete_note', kwargs={'pk': 1}),
					data={
						'text': ''
					},
					headers={
						'Authorization': f'JWT {token}'
					}
				)
				print(Note.objects.get(pk=1))
				self.assertEqual(res.status_code, status.HTTP_200_OK)

		def test_delete_note(self):
				token = self.client.post(
					reverse('login'),
					data={
						'email': 'example@example.com',
						'password': 'Uytrewq123'
					}
				).json()['token']
				res = self.client.delete(
					reverse('get_update_delete_note', kwargs={'pk': 1}),
					headers={
						'Authorization': f'JWT {token}'
					}
				)
				self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

		def test_list_todo(self):
				token = self.client.post(
					reverse('login'),
					data={
						'email': 'example@example.com',
						'password': 'Uytrewq123'
					}
				).json()['token']
				res = self.client.get(
					reverse('list_create_todo'),
					headers={
						'Authorization': f'JWT {token}'
					}
				)
				self.assertEqual(res.status_code, status.HTTP_200_OK)

		def test_create_todo(self):
				token = self.client.post(
					reverse('login'),
					data={
						'email': 'example@example.com',
						'password': 'Uytrewq123'
					}
				).json()['token']
				res = self.client.post(
					reverse('list_create_todo'),
					data = {
						'text': 'Second todo'
					},
					headers={
						'Authorization': f'JWT {token}'
					}
				)
				self.assertEqual(res.status_code, status.HTTP_201_CREATED)

		def test_retrieve_todo(self):
				token = self.client.post(
					reverse('login'),
					data={
						'email': 'example@example.com',
						'password': 'Uytrewq123'
					}
				).json()['token']
				res = self.client.get(
					reverse('get_update_delete_todo', kwargs={'pk': 1}),
					headers={
						'Authorization': f'JWT {token}'
					}
				)
				self.assertEqual(res.status_code, status.HTTP_200_OK)

		def test_update_todo(self):
				token = self.client.post(
					reverse('login'),
					data={
						'email': 'example@example.com',
						'password': 'Uytrewq123'
					}
				).json()['token']
				res = self.client.put(
					reverse('get_update_delete_todo', kwargs={'pk': 1}),
					data={
						'text': ''
					},
					headers={
						'Authorization': f'JWT {token}'
					}
				)
				print(Note.objects.get(pk=1))
				self.assertEqual(res.status_code, status.HTTP_200_OK)

		def test_delete_todo(self):
				token = self.client.post(
					reverse('login'),
					data={
						'email': 'example@example.com',
						'password': 'Uytrewq123'
					}
				).json()['token']
				res = self.client.delete(
					reverse('get_update_delete_todo', kwargs={'pk': 1}),
					headers={
						'Authorization': f'JWT {token}'
					}
				)
				self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)