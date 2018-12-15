from flask import Flask, request, abort, send_file
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage,
    ImageMessage, ImageSendMessage,
    TextSendMessage,
    StickerSendMessage,
    TemplateSendMessage,
    CarouselTemplate,
    CarouselColumn,
    CameraAction,
    CameraRollAction,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent, URIAction,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent, SeparatorComponent
)
from PIL import Image
from io import BytesIO
import numpy as np
from time import strftime
from subprocess import run
import pyimgur
from test import inference
import cv2
from template import score_bubble, help_prompt
from templateBubble import generate_report, classification_helper
from subprocess import check_output
price_report = None

app = Flask(__name__)
CLIENT_ID = '068f642d85cf4ba'
line_bot_api = LineBotApi(
    'Tgeyf75DpBpNorwq9mDXKWjUs5EgAMfCYpSzvKjUEIwIwOO2kVxoo0Bzj7XnP4VLaHM/JIH5m5qWMVlqizkUA/2YgvOjvYNJDY6+R60Px68gTyjbXURVueaHHt4eIiwlBXp00koWHGqgI3iYCKiYjAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('da2d6f9e4ea684b0141df09cfeb0bb89')

images_collection = {}

def format_float(float):
   return '{:.2f}'.format(float)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    reply = None
    if message == '上傳評分':
        reply = help_prompt
    elif message == '價格查詢':
        query_time = check_output(["python3", "scrape.py"])
        data = np.loadtxt('scraped.txt').tolist()
        data = list(map(format_float, data))
        print(data, query_time)
        price_report = generate_report(data[:3], data[3:], query_time.decode('ascii').strip())
        reply = price_report
    elif message == '分級撇步':
        reply = classification_helper
    #elif len(message) > 1 and message[0] == '-':
    #    run(message[1:].split(' '))
    #    return
    #elif len(message) > 1 and message[0] == '+':
    #    img_name = message[1:]
    #    link = images_collection[img_name]
    #    reply = ImageSendMessage(
    #            original_content_url=link, preview_image_url=link)
    #elif message.isdigit():
    #    reply = StickerSendMessage(package_id='1', sticker_id=message)
    else:
        reply = TextSendMessage(text=message)
    line_bot_api.reply_message(event.reply_token, reply)


@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    image = line_bot_api.get_message_content(event.message.id)
    try:
        '''
        fileName = strftime('%Y-%m-%d_%H:%M:%S')
        with open(fileName, 'wb+') as f:
            for byte in image.iter_content():
                f.write(byte)
        '''
        img_raw = b''.join(image.iter_content())
        img = Image.open(BytesIO(img_raw))
        img_arr = np.array(img)
        output = inference(img_arr)
        output = int(output)
        reply = score_bubble(output)
        line_bot_api.reply_message(
            event.reply_token, reply)
    except ValueError:
        print('err')

if __name__ == "__main__":
    app.run(ssl_context=('/etc/nginx/ssl/cert.pem', '/etc/nginx/ssl/cert.key'), port = 8081)
