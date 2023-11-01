import re

import scrapy

from urllib.parse import urljoin
from Assistant_scrapy.items import AssistantScrapyItem

class 贵州大学硕士招生Spider(scrapy.Spider):
    name = "贵州大学_硕士招生"
    allowed_domains = ["gs.gzu.edu.cn"]
    start_urls = ["http://gs.gzu.edu.cn/sszs/list.htm"]
    page_url = 'http://gs.gzu.edu.cn/sszs/list{}.htm'
    count = 0

    def parse(self, response):
        self.count += 1
        total_list = response.xpath('//div[@id="wp_news_w7"]//tr//li')
        for i in total_list:
            url = i.xpath('.//div[@class="list_cont_title"]/a/@href').extract_first()
            url = urljoin(self.start_urls[0], url)
            meta = {
                'title': i.xpath('.//div[@class="list_cont_title"]/a/@title').extract_first(),
                'url': url
            }
            yield scrapy.Request(url, meta=meta, callback=self.parse_item)

        #分页
        if self.count == 1:
           total_page = int(re.findall('sszs/list(\d+).htm" target="_self"><span>尾页', response.text)[0])
           print('----------', total_page)
           for i in range(2, total_page + 1):
                url = self.page_url.format(i)
                yield scrapy.Request(url, dont_filter=True)

    def parse_item(self, response):
        item = AssistantScrapyItem()

        title = response.xpath('//div[@class="Article_bt"]/div/div/text()').extract_first()
        time = response.xpath('//div[@class="Article_ly"]/div[2]/span[2]/text()').extract_first()
        content = response.xpath('//div[@id="tablePrint"]').extract_first()

        item['title'] = title
        item['time'] = time
        item['url'] = response.meta['url']
        item['content'] = content

        yield item


