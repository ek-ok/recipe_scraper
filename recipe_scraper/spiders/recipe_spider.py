# -*- coding: utf-8 -*-
import scrapy


class RecipeSpider(scrapy.Spider):
    name = 'recipe'
    allowed_domains = ['https://www.bigoven.com/']
    recipe_url = 'https://www.bigoven.com/recipe/'

    def start_requests(self):
        for i in range(10):
            url = self.recipe_url + str(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.status == 200:
            for quote in response.css('div.quote'):
                yield {
                    'text': quote.css('span.text::text').extract_first(),
                    'author': quote.css('small.author::text').extract_first(),
                    'tags': quote.css('div.tags > a.tag::text').extract()
                }
