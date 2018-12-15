from linebot.models import (
    MessageEvent,
    CarouselContainer,
    FlexSendMessage, BubbleContainer, BoxComponent,
    TextComponent, SeparatorComponent, ImageComponent
)
def item_key(text):
    return TextComponent(text=text, size="sm", color="#555555", flex=0)


def item_value(text):
    return TextComponent(text=text, size="sm", color="#111111", align="end")

def item(key, value):
    return BoxComponent(layout="horizontal", contents=[key, value])

def generate_item(item_pair):
    return item(item_key(item_pair[0]), item_value(item_pair[1]))


def generate_bubble(category, title, subtitle, data1, data2, footer):
    data2[0].margin = "xxl"
    return BubbleContainer(
        body=BoxComponent(
            layout="vertical",
            contents=[
                TextComponent(text=category, weight="bold", color="#1DB446", size="sm"),
                TextComponent(text=title, weight="bold", size="xxl", margin="md"),
                TextComponent(text=subtitle, color="#aaaaaa", size="xs", wrap=True),
                SeparatorComponent(margin="xxl"),
                BoxComponent(
                    layout="vertical",
                    margin="xxl",
                    spacing="sm",
                    contents=[*data1, SeparatorComponent(margin="xxl"), *data2]
                ),
                SeparatorComponent(margin="xxl"),
                BoxComponent(
                    layout="horizontal",
                    margin="md",
                    contents=[
                        TextComponent(text=footer[0], size="xs", color="#aaaaaa", flex=0),
                        TextComponent(text=footer[1], size="xs", color="#aaaaaa", align="end")
                    ]
                )
            ]
        ),
        styles={
            "footer": {
                "separator": True
            }
        }
    )

def generate_column(url, title, description):
    return BubbleContainer(
        hero=ImageComponent(
            url=url,
            size='full',
            aspect_ratio='20:13',
            aspect_mode='cover'
        ),
        body=BoxComponent(
            layout="vertical",
            spacing="sm",
            contents=[
                TextComponent(text=title, weight="bold", size="xl", wrap=True),
                TextComponent(text=description, size="md", wrap=True)
            ]
        )
    )

def generate_report(price, misc, time):
    return FlexSendMessage(alt_text="報價", contents=generate_bubble("價格查詢", "百香果", "全國平均",
        map(generate_item, list(zip(("特級", "優級", "良級"), price))),
        list(map(generate_item, list(zip(("平均價", "與前一交易日比較", "交易量", "與前一交易日比較"), misc)))),
        ("查詢時間", time)))


classification_helper = FlexSendMessage(
    alt_text="分類小幫手",
    contents=CarouselContainer(
        contents=[
            generate_column(url='https://i.imgur.com/fZwe7zF.png', title="特級", description="同一品種，成熟適度，果形完整，色澤優良，無病蟲害及其他傷害。"),
            generate_column(url='https://i.imgur.com/ndUWLAh.png', title="優級", description="同一品種，成熟尚適度，果形尚完整，色澤良好，無嚴重病蟲害及其他傷害"),
            generate_column(url='https://i.imgur.com/YoKRHdP.png', title="良級", description="品質次於優級品，但有商品價值者。")
        ]
    )
)