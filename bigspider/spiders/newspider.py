import scrapy
import pandas as pd


class MySpider(scrapy.Spider):
    name = 'newspider'
    allowed_domains = ['lifehack.org']
    start_urls = ['https://www.lifehack.org/articles/featured/how-to-find-your-passion.html']

    def parse(self, response):
       # classes = response.css('div::attr(class)').getall()
        data = pd.read_csv('../easylist.txt', error_bad_lines=False)
        for row in data.iterrows():
            print('g' +'"'+str(row)+'"'+'+')
            classes = response.xpath('//div[contains(@class, '+'"'+str(row)+'"'+')]/@class').getall()
            print(classes)
            if not classes:
                print("NO ADS BABY")
            else:
                print("there are ads")





