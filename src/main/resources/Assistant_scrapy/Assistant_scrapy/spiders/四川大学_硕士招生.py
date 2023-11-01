import re

import scrapy

from urllib.parse import urljoin
from Assistant_scrapy.items import AssistantScrapyItem

class A四川大学硕士招生Spider(scrapy.Spider):
    name = "四川大学_硕士招生"
    allowed_domains = ["yz.scu.edu.cn"]
    start_urls = ["https://yz.scu.edu.cn/zsxx/newslist/ss/gg"]
    page_url = 'http://gs.gzu.edu.cn/sszs/list{}.htm'
    count = 0

    def parse(self, response):
        self.count += 1
        total_list = response.xpath('//div[@class="col-md-9 col-sm-9 content-one col-xs-12"]/ul/li')
        for i in total_list:
            url = i.xpath('.//a/@href').extract_first()
            url = urljoin(self.start_urls[0], url)
            meta = {
                'title': i.xpath('.//a/text()').extract_first(),
                'time': i.xpath('.//span[2]/text()').extract_first(),
                'url': url
            }
            yield scrapy.Request(url, meta=meta, callback=self.parse_item)

        # 分页
        if self.count == 1:
            total_page = int(re.findall('/gg(\d+)">尾页', response.text)[0])
            print('----------', total_page)
            for i in range(2, total_page + 1):
                url = self.page_url.format(i)
                yield scrapy.Request(url, dont_filter=True)

    def parse_item(self, response):
        item = AssistantScrapyItem()

        item['title'] = response.meta['title']
        title = response.xpath('//div[@class="col-md-9 col-sm-9 content-one col-xs-12"]/h2/text()').extract_first()
        title = response.xpath('//div[@class="col-md-9 col-sm-9 content-one col-xs-12"]/h2/text()').extract_first()
        title = response.xpath('//h3[@class="content-title"]/h2/text()').extract_first()

        item['time'] = response.meta['time']

        time = response.xpath('//div[@class="Article_ly"]/div[2]/span[2]/text()').extract_first()

        content = response.xpath('//table[@class="table-inquiry"]').extract_first()
        item.values('content', response.xpath('//div[@class="content-box"]'))

        item['title'] = title
        item['time'] = time
        item['url'] = response.meta['url']
        item['content'] = content
        item['college'] = '四川大学_硕士招生'

        yield item