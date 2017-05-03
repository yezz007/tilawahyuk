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
    print(request.META['HTTP_X_LINE_SIGNATURE'])
    body = str(request.body)
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        HttpResponse(status=400)
    return HttpResponse(status=200)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Hello world!"))