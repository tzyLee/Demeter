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

def score_bubble(CLASS):
   title = None
   description = None
   image_url = None
   stars = None
   
   if CLASS == 0:
      title = '良級'
      description = '品質次於優級品，但有商品價值者。'
      image_url = 'https://i.imgur.com/YoKRHdP.png'
      stars = 1   
   elif CLASS == 1:
      title = '優級'
      description = '同一品種，成熟尚適度，果形尚完整，色澤良好，無嚴重病蟲害及其他傷害。'
      image_url = 'https://i.imgur.com/ndUWLAh.png'
      stars = 3
   elif CLASS == 2:
      title = '特級'
      description = '同一品種，成熟適度，果形完整，色澤優良，無病蟲害及其他傷害。'
      image_url = 'https://i.imgur.com/fZwe7zF.png'
      stars = 5
   stars_contents = []

   for i in range(stars):
      stars_contents.append(IconComponent(size='md', url='https://i.imgur.com/qGdfV69.png')) # gold star
   while len(stars_contents) < 5:
      stars_contents.append(IconComponent(size='md', url='https://i.imgur.com/YYw2wxe.png')) # black star

   stars_contents.append(TextComponent(text=str(stars), size='sm', color='#999999', margin='md', flex=0))

   bubble=FlexSendMessage(alt_text="評分結果", contents=BubbleContainer(
      direction='ltr',
      header=BoxComponent(
         layout='vertical',
         contents=[
            TextComponent(text='品質分析', weight='bold', size='xl')     
         ]
      ),
      hero=ImageComponent(
         url=image_url,
         size='full',
         aspect_ratio='20:13',
         aspect_mode='cover'
      ),
      body=BoxComponent(
         layout='vertical',
         contents=[
             TextComponent(text=title, size='lg'),
             BoxComponent(
                 layout='baseline',
                 margin='md',
                 contents=stars_contents
             ),
             TextComponent(text=description, wrap=True, size='md')
         ]
      )
   ))
   return bubble

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


