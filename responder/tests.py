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

#body = '{"events":[{"type":"message","replyToken":"701d0e140317460aaa29ff68e2beb2c6","source":{"userId":"Ue75b6ee1c1e794355294af4d63966f40","type":"user"},"timestamp":1493881541099,"message":{"type":"text","id":"6034136262874","text":"Tes"}}]}\'2017-05-04T07:05:42.264264+00:00 app[web.1]: {\'SERVER_SOFTWARE\': \'gunicorn/19.7.1\', \'wsgi.errors\': <gunicorn.http.wsgi.WSGIErrorsWrapper object at 0x7fbbea62ae80>, \'HTTP_X_REQUEST_START\': \'1493881541810\', \'wsgi.url_scheme\': \'https\', \'HTTP_X_FORWARDED_PROTO\': \'https\', \'PATH_INFO\': \'/callback/\', \'SERVER_PROTOCOL\': \'HTTP/1.1\', \'HTTP_X_FORWARDED_FOR\': \'203.104.146.154\', \'CONTENT_TYPE\': \'application/json;charset=UTF-8\', \'HTTP_TOTAL_ROUTE_TIME\': \'0\', \'wsgi.file_wrapper\': <class \'gunicorn.http.wsgi.FileWrapper\'>, \'RAW_URI\': \'/callback/\', \'wsgi.run_once\': False, \'HTTP_X_FORWARDED_PORT\': \'443\', \'HTTP_X_REQUEST_ID\': \'8e51ab27-93e1-494f-b91a-5e5b26307427\', \'HTTP_CONNECTION\': \'close\', \'HTTP_VIA\': \'1.1 vegur\', \'HTTP_USER_AGENT\': \'LineBotWebhook/1.0\', \'SERVER_PORT\': \'50418\', \'HTTP_CONNECT_TIME\': \'1\', \'wsgi.multiprocess\': True, \'HTTP_X_LINE_SIGNATURE\': \'VAPryQiivtqFN4vomSmyr/pej8iZvqgUw3ayX6Flrrc=\', \'REQUEST_METHOD\': \'POST\', \'wsgi.input\': <gunicorn.http.body.Body object at 0x7fbbea62add8>, \'REMOTE_ADDR\': \'10.186.38.2\', \'wsgi.multithread\': False, \'wsgi.version\': (1, 0), \'REMOTE_PORT\': \'53450\', \'HTTP_HOST\': \'yuktilawah.herokuapp.com\', \'gunicorn.socket\': <socket.socket fd=10, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=(\'172.19.1.226\', 50418), raddr=(\'10.186.38.2\', 53450)>, \'SCRIPT_NAME\': \'\', \'CONTENT_LENGTH\': \'235\', \'HTTP_ACCEPT\': \'*/*\', \'SERVER_NAME\': \'0.0.0.0\', \'QUERY_STRING\': \'\'}'     
#body = '{"events":[{"type":"message","replyToken":"701d0e140317460aaa29ff68e2beb2c6","source":{"userId":"Ue75b6ee1c1e794355294af4d63966f40","type":"user"},"timestamp":1493881541099,"message":{"type":"text","id":"6034136262874","text":"Tes"}}]}'