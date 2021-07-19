from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class RequestsTestCase(TestCase):
		def test_save_request(self):
				res = self.client.get(reverse('save_request'))
				self.assertEqual(res.status_code, status.HTTP_200_OK)

		def test_get_filtered_requests(self):
				res = self.client.get(reverse('filtered_requests'))
				self.assertEqual(res.status_code, status.HTTP_200_OK)