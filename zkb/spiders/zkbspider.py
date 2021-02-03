import scrapy
from ..items import ZkbItem


class ZkbspiderSpider(scrapy.Spider):
    name = 'zkbspider'
    allowed_domains = ['www.zkb-oe.at/de/kontakt-services/presse-news/podcast/']
    start_urls = ['http://www.zkb-oe.at/de/kontakt-services/presse-news/podcast/']

    def parse(self, response):

        item = ZkbItem()
        articles = response.xpath('//section[@id="c564"]//div[@class="box-inner box-padding"]')
        for article in articles:
            date = article.xpath('./p[1]/text()').get()
            caption = article.xpath('./h2/text()').get()
            content = ''.join(article.xpath('./p[2]/text()').getall())

            item['date'] = date
            item['caption'] = caption
            item['content'] = content

            yield item