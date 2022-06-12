from scrapy.crawler import CrawlerProcess
from libc.crawl import VnExpressSpider, Kenh14Spider, DantriSpider, DevToApi, ThanhnienSpider    
import scrapy
import re
from datetime import datetime
from bs4 import BeautifulSoup

class GenkSpider(scrapy.Spider):
    name = "genk"
    start_urls = [
        'https://genk.vn',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'libc.mysql_pipe.MysqlWriterPipeline': 1}, # Used for pipeline 1
    }

    def parse_content(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.body, 'html.parser')
        bodyElem = soup.select_one('div.kbwc-body')
        item['content'] = ''
        if bodyElem is not None:
            item['content'] = bodyElem.get_text()
        item['domain'] = self.start_urls[0]
        return item

    def parse(self, response):
        for quote in response.css('h4.knswli-title > a'):
            detail_url = quote.css('a::attr("href")').extract_first()
            print('detail_url', detail_url)
            if detail_url is not None:
                item = {
                    'title': quote.css('a::text').extract_first(),
                    'url': detail_url,
                }
                request = scrapy.Request(response.urljoin(detail_url), callback=self.parse_content)
                request.meta['item'] = item
                yield request

def lambda_handler(event, context):
    print(event)
    # try:
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    # process.crawl(VnExpressSpider)
    process.crawl(GenkSpider)
    # process.crawl(Kenh14Spider)
    # process.crawl(DantriSpider)
    # process.crawl(ThanhnienSpider)
    # process.crawl(DevToApi)

    process.start()

    # except Exception as err:
    #     print('err:', err)




