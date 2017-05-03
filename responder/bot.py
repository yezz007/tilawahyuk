from tilawahyuk.settings import LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from django.http import HttpResponse

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

def base(request):
    print(request.scheme)
    print(request.encoding)
    print(request.content_type)
    print(request.body)
    print(request.META)
    return HttpResponse(status=200)