from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem

class StackSpider(Spider):
    name = 'stack'
    allowed_domains = 'stackoverflow.com'
    start_urls = ['https://stackoverflow.com/questions/tagged/python?sort=featured&pageSize=30']

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]')
        items = []

        for question in questions:
            item = StackItem()
            title = question.xpath('//a[@class="question-hyperlink"]/text()').extract()
            url = question.xpath('//a[@class="question-hyperlink"]/@href').extract()
            item['title'] = title
            item['url'] = url
            items.append(item)

        return item

