import scrapy

sites = ['mirror.xyz', 
         'jessicadw.com/',
         'tinybuddha.com/',
         'geohot.com/']

class MySpider(scrapy.Spider):
    name = 'newspider'
    allowed_domains = sites
    start_urls = ['https://jessicadw.com/blog/find-your-passion',
                  'https://tinybuddha.com/blog/try-this-if-youre-struggling-to-find-your-passion/',]

    def parse(self, response):
        print(response.css('script::text').get())
