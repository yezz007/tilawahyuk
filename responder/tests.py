from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class UserSetViewTests(TestCase):
	def test_isOk(self):
		response = self.client.get(reverse('responder:user-list'))
		self.assertEqual(response.status_code, 200)