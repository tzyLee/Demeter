import scrapy
from scrapy.crawler import CrawlerProcess
import re
import numpy as np
from time import strftime
import datetime as d
import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

class HTMLTableSaver:
    signedNumber = re.compile(r'([+-]?) *(\d+)$')
    def __init__(self):
        self.result = []

    def feed(self, data):
        self.result.append(data)

    def process(self):
        numOfMarket = len(self.result[2])//9 - 1
        temp = []
        for i in range(numOfMarket):
            temp.append(list(map(HTMLTableSaver.parseNumber, self.result[2][14+9*i:21+9*i]))) # replace 14 with 12 if want to keep first two col
        temp = np.nanmean(np.array(temp, dtype=np.float), axis=0)
        print(self.result[1][3]) #output to stdout
        self.result[2][2:5] = ['特級', '優級', '良級']
        np.savetxt('scraped.txt', temp)
    
    @staticmethod
    def parseNumber(string):
        result = re.match(HTMLTableSaver.signedNumber, string)
        if not result:
            try:
                if string.strip() == '-':
                    string = 'nan'
                return locale.atof(string)
            except ValueError:
                return string
        elif result[1] == '-':
            return -locale.atof(result[2])
        return locale.atof(result[2])



formdata = {
    "ctl00$ScriptManager_Master": 'ctl00$ScriptManager_Master|ctl00$contentPlaceHolder$btnQuery',
    "ctl00$contentPlaceHolder$ucDateScope$rblDateScope": "D",  # Single Day
    "ctl00$contentPlaceHolder$ucSolarLunar$radlSolarLunar": "S",  # 國曆
    "ctl00$contentPlaceHolder$txtSTransDate": '107/12/09',  # Start day
    "ctl00$contentPlaceHolder$txtETransDate": '107/12/10',  # End day
    "ctl00$contentPlaceHolder$txtMarket": '全部市場',
    "ctl00$contentPlaceHolder$hfldMarketNo": 'ALL',  # 所有市場
    "ctl00$contentPlaceHolder$txtProduct": '50 百香果 其他',  # 產品文字
    "ctl00$contentPlaceHolder$hfldProductNo": '50',  # 產品ID
    "ctl00$contentPlaceHolder$hfldProductType": 'S',
    "ctl00$contentPlaceHolder$btnQuery": '查詢',  # 查詢按鈕
    "__EVENTTARGET": '',
    "__EVENTARGUMENT": '',
    "__ASYNCPOST": 'true'
}


class ViewStateSpider(scrapy.Spider):
    name = 'spidyquotes-viewstate'
    start_urls = ['https://amis.afa.gov.tw/fruit/FruitProdDayTransInfo.aspx']
    download_delay = 1.5

    def parse(self, response):
        formdata["__VIEWSTATE"] = response.css(
            'input#__VIEWSTATE::attr(value)').extract_first()
        formdata["__VIEWSTATEGENERATOR"] = response.css(
            'input#__VIEWSTATEGENERATOR::attr(value)').extract_first()
        formdata["__EVENTVALIDATION"] = response.css(
            'input#__EVENTVALIDATION::attr(value)').extract_first()
        yield scrapy.FormRequest(
            self.start_urls[0],
            formdata=formdata,
            callback=self.parse_results
        )

    def parse_results(self, response):
        parser = HTMLTableSaver()
        for quote in response.css("div#ctl00_contentPlaceHolder_panel > table").extract():
            sel = scrapy.Selector(text=quote)
            parser.feed(list(filter(bool, (j.strip() for i in sel.xpath('string(.)').extract() for j in i.split('\r\n') if not i.isspace()))))
            # parser.feed(list(filter(bool, (j.strip() for i in sel.xpath('string(.)').extract() for j in i.split('\r\n') if not i.isspace()))))
        parser.process()


class DataScraper:
    def __call__(self):
        today = d.date.today()
        today = today.replace(year=today.year-1911)
        formdata["ctl00$contentPlaceHolder$txtSTransDate"] = today.strftime('%Y/%m/%d')
        formdata["ctl00$contentPlaceHolder$txtETransDate"] = (today+d.timedelta(days=1)).strftime('%Y/%m/%d')
        process = CrawlerProcess(
            {'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})
        process.crawl(ViewStateSpider)
        process.start()  # the script will block here until the crawling is finished


if __name__ == '__main__':
    ds = DataScraper()
    ds()
