from linebot.models import (
    MessageEvent,
    FlexSendMessage, BubbleContainer, BoxComponent,
    TextComponent, SeparatorComponent
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

price_report = FlexSendMessage(alt_text="報價", contents=generate_bubble("價格查詢", "百香果", "全國平均",
    map(generate_item, [("上價", "52.7"), ("中價", "24.7"), ("下價", "9.6")]),
    list(map(generate_item, [("平均價", "27.3"), ("與前一交易日比較", "+53%"), ("交易量", "657"), ("與前一交易日比較", "-52%")])),
    ("查詢時間", "107/12/08 13:00:37")))