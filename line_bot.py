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

app = Flask(__name__)
CLIENT_ID = '068f642d85cf4ba'
#im = pyimgur.Imgur(CLIENT_ID)
line_bot_api = LineBotApi(
    'Tgeyf75DpBpNorwq9mDXKWjUs5EgAMfCYpSzvKjUEIwIwOO2kVxoo0Bzj7XnP4VLaHM/JIH5m5qWMVlqizkUA/2YgvOjvYNJDY6+R60Px68gTyjbXURVueaHHt4eIiwlBXp00koWHGqgI3iYCKiYjAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('da2d6f9e4ea684b0141df09cfeb0bb89')

images_collection = {}

bubble = FlexSendMessage(alt_text="help", contents=BubbleContainer(
    direction='ltr',
    hero=ImageComponent(
        url='https://i.pinimg.com/originals/e6/4a/ab/e64aabf950b63781ce7ae2d05ce026dd.png',
        size='full',
        aspect_ratio='20:13',
        aspect_mode='cover'
    ),
    body=BoxComponent(
        layout='vertical',
        contents=[
            TextComponent(text='品質偵測', weight='bold', size='xl'),
            BoxComponent(
                layout='baseline',
                margin='md',
                contents=[
                    IconComponent(
                        size='md', url='https://i.imgur.com/qGdfV69.png'),
                    IconComponent(
                        size='md', url='https://i.imgur.com/qGdfV69.png'),
                    IconComponent(
                        size='md', url='https://i.imgur.com/qGdfV69.png'),
                    IconComponent(
                        size='md', url='https://i.imgur.com/qGdfV69.png'),
                    IconComponent(
                        size='md', url='https://i.imgur.com/3g5n4Wv.png'),
                    TextComponent(text='4.0', size='sm',
                                  color='#999999', margin='md', flex=0)
                ]
            )
        ],
    ),
    footer=BoxComponent(
        layout='vertical',
        spacing='sm',
        contents=[
            SpacerComponent(size='sm'),
            ButtonComponent(
                style='link',
                height='sm',
                action=URIAction(label='TODO', uri='tel:000000'),
            ),
            SeparatorComponent()
        ]
    ),
))

help_prompt = TemplateSendMessage(
    alt_text='幫助選單',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://i.imgur.com/WAqchIp.jpg',
                title='幫助選單',
                text='拍照或上傳照片即可為您進行評分',
                actions=[
                    CameraAction(
                        label='拍照',
                        text='camera'
                    ),
                    CameraRollAction(
                        label='上傳',
                        text='camera roll'
                    )
                ]
            )
        ]
    )
)

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
    elif message == '測試':
        reply = bubble
    elif len(message) > 1 and message[0] == '-':
        run(message[1:].split(' '))
        return
    elif len(message) > 1 and message[0] == '+':
        img_name = message[1:]
        link = images_collection[img_name]
        reply = ImageSendMessage(
                original_content_url=link, preview_image_url=link)
    elif message.isdigit():
        reply = StickerSendMessage(package_id='1', sticker_id=message)
    else:
        reply = TextSendMessage(text=message)
    line_bot_api.reply_message(event.reply_token, reply)


@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    image = line_bot_api.get_message_content(event.message.id)
    # print(image)
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
        print('img_arr', img_arr)
        output = inference(img_arr)
        print('output', output)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=f'Class {output}'))
        
        #uploaded = im.upload_image(fileName, title=fileName)
        #images_collection[fileName] = uploaded.link
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(
        #    text=f'Successfully uploaded to imgur, link is {uploaded.link}'))
    except ValueError:
        print('err')
    #    line_bot_api.reply_message(event.reply_token, TextSendMessage(
    #        text='Error occurred during uploading to imgur'))

if __name__ == "__main__":
    app.run(ssl_context=('/etc/nginx/ssl/cert.pem', '/etc/nginx/ssl/cert.key'), port = 8081)
