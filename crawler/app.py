from scrapy.crawler import CrawlerProcess
from lib.crawl import GenkSpider, VnExpressSpider, Kenh14Spider, DantriSpider, DevToApi, ThanhnienSpider    

def lambda_handler(event, context):
    print(event)
    try:
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

    except Exception as err:
        print('err:', err)




