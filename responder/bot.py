from tilawahyuk.settings import LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET
from linebot import (
    LineBotApi, WebhookHandler, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from django.http import HttpResponse

#import logging

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)
parser = WebhookParser(LINE_CHANNEL_SECRET)
#logger = logging.getLogger(__name__)

def base(request):
    print('token:', LINE_CHANNEL_ACCESS_TOKEN)
    print('secret:', LINE_CHANNEL_SECRET)
    print(request.scheme)
    print(request.encoding)
    print(request.content_type)
    print(request.body)
    print(request.META)
    if 'HTTP_X_LINE_SIGNATURE' not in request.META:
        return HttpResponse(status=200)
    print(request.META['HTTP_X_LINE_SIGNATURE'])
    body = str(request.body)
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        HttpResponse(status=400)
    events = parser.parse(body, signature)
    for event in events:
        print('event:', event)
        line_bot_api.reply_message( event.reply_token, TextSendMessage(text=event.message.text))
    return HttpResponse(status=200)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Hello world!"))