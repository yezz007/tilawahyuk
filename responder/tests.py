from django.test import TestCase
from django.urls import reverse
from tilawahyuk.settings import LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET

# Create your tests here.
class UserSetViewTests(TestCase):
	def test_isOk(self):
		response = self.client.get(reverse('responder:user-list'))
		self.assertEqual(response.status_code, 200)

class SettingsTester(TestCase):
	def test_settings(self):
		self.assertNotEqual(LINE_CHANNEL_SECRET, '')
		self.assertNotEqual(LINE_CHANNEL_ACCESS_TOKEN, '')